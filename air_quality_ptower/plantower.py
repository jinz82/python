import serial

class pt_pms5003():
    """Plantower PMS5003 sensor class, makes full structure of sensor functionality"""
    def __init__(self,serialport,timeout=1,samples=5):
        """Initialize constructors for an instance"""
        self.serialport     = serialport
        self.timeout        = timeout
        self.samples        = samples
        self.baud_rate      = 9600
        self.parity         = serial.PARITY_NONE
        self.stopbits       = serial.STOPBITS_ONE
        self.bytesize       = serial.EIGHTBITS
        
        # Try to open the serial port here itself.
        self.serial_handle  = serial.Serial(port=self.serialport, baudrate=self.baud_rate, parity=self.parity,
                                            stopbits=self.stopbits, bytesize=self.bytesize, timeout=self.timeout)

        # PMS packet properties.
        self.pms_packet_start1  = 'B'
        self.pms_packet_start2  = 'M'
        self.pms_packet_size    = 28
        self.pms_list           = []
        # Storage for AQI index values and averages.

        self.aqi_sum_pm_01_0 = 0
        self.aqi_sum_pm_02_5 = 0
        self.aqi_sum_pm_10_0 = 0

        self.aqi_avg_pm_01_0 = 0
        self.aqi_avg_pm_02_5 = 0
        self.aqi_avg_pm_10_0 = 0

        self.aqi_pm_01_0 = 0
        self.aqi_pm_02_5 = 0
        self.aqi_pm_10_0 = 0

    def pt_avg_and_clr_all_PMS(self):
        """Averages and clears all PM values (1.0, 2.5 and 10.0)"""
        self.aqi_avg_pm_01_0 = (self.aqi_sum_pm_01_0/self.samples)
        self.aqi_avg_pm_02_5 = (self.aqi_sum_pm_02_5/self.samples)
        self.aqi_avg_pm_10_0 = (self.aqi_sum_pm_10_0/self.samples)
        self.aqi_sum_pm_01_0 = 0
        self.aqi_sum_pm_02_5 = 0
        self.aqi_sum_pm_10_0 = 0
        
    def pt_word_value(self, aqi_list):
        """Return value of the word"""
        word_value = 256*(aqi_list[0])+(aqi_list[1])
        return word_value

    def pt_pkt_chksum(self, pkt_list):
        """Evaluate checksum"""
        pkt_checksum = 0
        for item in pkt_list:
            pkt_checksum += item
        return pkt_checksum

    def pt_read_pktheader(self):
        """Reads packet header start of frame and packet length"""
        while True:
            # Read line at a time neglect it if not meaningful.
            if (self.serial_handle.read() == self.pms_packet_start1) and (self.serial_handle.read() == self.pms_packet_start2):
                # Looks worthy of look.
                frame_h = ord(self.serial_handle.read())
                frame_l = ord(self.serial_handle.read())
                # Packet length should be a known value.
                if (((256*frame_h)+frame_l) == self.pms_packet_size):
                    for pkt in range(0,self.pms_packet_size):
                        self.pms_list.append(ord(self.serial_handle.read()))
                    return

    def pt_read_singlepacket(self):
        """Read single PMS packet"""
        pm_01_0 = 0
        pm_02_5 = 0
        pm_10_0 = 0

        if (self.pt_pkt_chksum(self.pms_list[0:26]) + ord(self.pms_packet_start1) + ord(self.pms_packet_start2) + self.pms_packet_size  == self.pt_word_value(self.pms_list[26:28])) and (len(self.pms_list) == self.pms_packet_size):
            pms_01_0 = self.pt_word_value(self.pms_list[0:2])
            pms_02_5 = self.pt_word_value(self.pms_list[2:4])
            pms_10_0 = self.pt_word_value(self.pms_list[4:6])

            pm_01_0  = self.pt_word_value(self.pms_list[6:8])
            pm_02_5  = self.pt_word_value(self.pms_list[8:10])
            pm_10_0  = self.pt_word_value(self.pms_list[10:12])
            
            self.pms_list[:]=[]
            return pm_01_0, pm_02_5,pm_10_0
        else:
            self.pms_list[:]=[]
            return pm_01_0, pm_02_5,pm_10_0

    def pt_pms5003_read(self):
        """Reads samples and returns the PM stats"""
        temp_pm_01_0 = 0
        temp_pm_02_5 = 0
        temp_pm_10_0 = 0
        
        for sample in range(0,self.samples):
            self.pt_read_pktheader()
            temp_pm_01_0,temp_pm_02_5,temp_pm_10_0 = self.pt_read_singlepacket()
            """Got readings, read only if we think they are right"""
            if temp_pm_01_0:
                self.aqi_sum_pm_01_0 += temp_pm_01_0 
                self.aqi_sum_pm_02_5 += temp_pm_02_5
                self.aqi_sum_pm_10_0 += temp_pm_10_0
            else:
                sample -=1
                print("NPKT")
                
        # Store averages and clear sum.
        self.pt_avg_and_clr_all_PMS()
        return self.aqi_avg_pm_01_0,self.aqi_avg_pm_02_5,self.aqi_avg_pm_10_0
