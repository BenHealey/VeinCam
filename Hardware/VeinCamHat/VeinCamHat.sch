EESchema Schematic File Version 4
LIBS:VeinCamHat-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "VeinCam RPi 3 A + Hat "
Date "2019-03-12"
Rev "0"
Comp "VeinCam2019 - Josh Johnson"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Notes 1350 850  0    100  ~ 0
RPi Connector
$Comp
L Mechanical:MountingHole H1
U 1 1 5C8828F4
P 1150 7000
F 0 "H1" H 1250 7046 50  0000 L CNN
F 1 "MountingHole" H 1250 6955 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1150 7000 50  0001 C CNN
F 3 "~" H 1150 7000 50  0001 C CNN
	1    1150 7000
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 5C882948
P 1150 7200
F 0 "H2" H 1250 7246 50  0000 L CNN
F 1 "MountingHole" H 1250 7155 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1150 7200 50  0001 C CNN
F 3 "~" H 1150 7200 50  0001 C CNN
	1    1150 7200
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 5C88296E
P 1150 7400
F 0 "H3" H 1250 7446 50  0000 L CNN
F 1 "MountingHole" H 1250 7355 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1150 7400 50  0001 C CNN
F 3 "~" H 1150 7400 50  0001 C CNN
	1    1150 7400
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 5C882996
P 1150 7600
F 0 "H4" H 1250 7646 50  0000 L CNN
F 1 "MountingHole" H 1250 7555 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 1150 7600 50  0001 C CNN
F 3 "~" H 1150 7600 50  0001 C CNN
	1    1150 7600
	1    0    0    -1  
$EndComp
Text Notes 1200 6850 0    100  ~ 0
M2.5
Wire Wire Line
	6900 1700 7250 1700
Wire Wire Line
	6900 1900 7250 1900
Wire Wire Line
	6900 2350 7250 2350
Wire Wire Line
	6900 2550 7250 2550
Wire Wire Line
	7850 2350 8200 2350
Wire Wire Line
	7850 1900 8200 1900
Wire Wire Line
	7850 1700 8200 1700
Wire Wire Line
	7850 2550 8200 2550
$Comp
L power:+5V #PWR06
U 1 1 5C8975EF
P 5500 1750
F 0 "#PWR06" H 5500 1600 50  0001 C CNN
F 1 "+5V" H 5500 1890 50  0000 C CNN
F 2 "" H 5500 1750 50  0000 C CNN
F 3 "" H 5500 1750 50  0000 C CNN
	1    5500 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	8800 2550 9000 2550
Wire Wire Line
	9000 2550 9000 2750
Wire Wire Line
	8800 1900 9000 1900
Wire Wire Line
	9000 1900 9000 2550
Connection ~ 9000 2550
$Comp
L Device:R R7
U 1 1 5C89F961
P 8600 3150
F 0 "R7" H 8670 3196 50  0000 L CNN
F 1 "10K" H 8670 3105 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 8530 3150 50  0001 C CNN
F 3 "~" H 8600 3150 50  0001 C CNN
	1    8600 3150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R8
U 1 1 5C89F9C9
P 10050 3150
F 0 "R8" H 10120 3196 50  0000 L CNN
F 1 "10K" H 10120 3105 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 9980 3150 50  0001 C CNN
F 3 "~" H 10050 3150 50  0001 C CNN
	1    10050 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	9000 3150 9000 3350
Wire Wire Line
	8600 3300 8600 3350
Wire Wire Line
	8600 3350 9000 3350
Connection ~ 9000 3350
Wire Wire Line
	9000 3350 9000 3450
Wire Wire Line
	8600 3000 8600 2950
Wire Wire Line
	8600 2950 8700 2950
Wire Wire Line
	10150 2950 10050 2950
Wire Wire Line
	10050 2950 10050 3000
Wire Wire Line
	10050 3300 10050 3350
Wire Wire Line
	10050 3350 10450 3350
Wire Wire Line
	10450 3350 10450 3150
Wire Wire Line
	10450 3350 10450 3450
Connection ~ 10450 3350
$Comp
L power:GND #PWR07
U 1 1 5C8B69B2
P 9000 3450
F 0 "#PWR07" H 9000 3200 50  0001 C CNN
F 1 "GND" H 9000 3300 50  0000 C CNN
F 2 "" H 9000 3450 50  0000 C CNN
F 3 "" H 9000 3450 50  0000 C CNN
	1    9000 3450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR08
U 1 1 5C8B6A2F
P 10450 3450
F 0 "#PWR08" H 10450 3200 50  0001 C CNN
F 1 "GND" H 10450 3300 50  0000 C CNN
F 2 "" H 10450 3450 50  0000 C CNN
F 3 "" H 10450 3450 50  0000 C CNN
	1    10450 3450
	1    0    0    -1  
$EndComp
Connection ~ 10050 2950
Wire Wire Line
	9600 2950 10050 2950
Text Notes 7300 1100 0    100  ~ 0
IR LED's
Wire Wire Line
	10450 1700 10450 2350
Wire Wire Line
	8800 1700 10450 1700
Wire Wire Line
	8800 2350 10450 2350
Text Notes 7350 1300 0    50   ~ 0
2->1 940nm\n3->4 850nm
Text Notes 3750 1550 0    100  ~ 0
Status LEDs
$Comp
L Device:R R1
U 1 1 5D25BF6E
P 4150 1900
F 0 "R1" V 4050 1850 50  0000 L CNN
F 1 "1K" V 4250 1850 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4080 1900 50  0001 C CNN
F 3 "~" H 4150 1900 50  0001 C CNN
	1    4150 1900
	0    1    1    0   
$EndComp
$Comp
L Device:LED D1
U 1 1 5D25BF75
P 4550 1900
F 0 "D1" H 4600 1800 50  0000 R CNN
F 1 "GREEN LED" H 4750 2000 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric" H 4550 1900 50  0001 C CNN
F 3 "~" H 4550 1900 50  0001 C CNN
	1    4550 1900
	-1   0    0    1   
$EndComp
Wire Wire Line
	1450 3850 1450 3900
Wire Wire Line
	1450 3900 1550 3900
Wire Wire Line
	2150 3900 2150 3850
Wire Wire Line
	2050 3850 2050 3900
Connection ~ 2050 3900
Wire Wire Line
	2050 3900 2150 3900
Wire Wire Line
	1950 3850 1950 3900
Connection ~ 1950 3900
Wire Wire Line
	1950 3900 2050 3900
Wire Wire Line
	1850 3850 1850 3900
Connection ~ 1850 3900
Wire Wire Line
	1850 3900 1950 3900
Wire Wire Line
	1750 3850 1750 3900
Connection ~ 1750 3900
Wire Wire Line
	1750 3900 1850 3900
Wire Wire Line
	1650 3850 1650 3900
Connection ~ 1650 3900
Wire Wire Line
	1650 3900 1750 3900
Wire Wire Line
	1550 3850 1550 3900
Connection ~ 1550 3900
Wire Wire Line
	1550 3900 1650 3900
$Comp
L power:GND #PWR03
U 1 1 5D37B906
P 2150 3950
F 0 "#PWR03" H 2150 3700 50  0001 C CNN
F 1 "GND" H 2150 3800 50  0000 C CNN
F 2 "" H 2150 3950 50  0000 C CNN
F 3 "" H 2150 3950 50  0000 C CNN
	1    2150 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	2150 3950 2150 3900
Connection ~ 2150 3900
Wire Wire Line
	1750 1250 1750 1200
Wire Wire Line
	1750 1200 1700 1200
Wire Wire Line
	1650 1200 1650 1250
Wire Wire Line
	1700 1200 1700 1150
Connection ~ 1700 1200
Wire Wire Line
	1700 1200 1650 1200
$Comp
L power:+5V #PWR02
U 1 1 5D444BB1
P 1700 1150
F 0 "#PWR02" H 1700 1000 50  0001 C CNN
F 1 "+5V" H 1715 1323 50  0000 C CNN
F 2 "" H 1700 1150 50  0001 C CNN
F 3 "" H 1700 1150 50  0001 C CNN
	1    1700 1150
	1    0    0    -1  
$EndComp
NoConn ~ 2650 1650
NoConn ~ 2650 1750
Wire Wire Line
	1050 2150 650  2150
Wire Wire Line
	2650 3350 3050 3350
Text Label 3050 3350 2    50   ~ 0
LED_940
Text Label 650  2150 0    50   ~ 0
LED_850
Text Label 8200 2950 0    50   ~ 0
LED_850
Wire Wire Line
	8600 2950 8200 2950
Connection ~ 8600 2950
Text Label 9600 2950 0    50   ~ 0
LED_940
Wire Wire Line
	10450 2350 10450 2750
Connection ~ 10450 2350
Text Label 600  3150 0    50   ~ 0
LED_READY
Wire Wire Line
	600  3150 1050 3150
Wire Wire Line
	600  2350 1050 2350
Text Label 600  2350 0    50   ~ 0
nLED_BOOT
Text Label 3500 1900 0    50   ~ 0
LED_READY
Text Label 3500 2550 0    50   ~ 0
nLED_BOOT
$Comp
L Device:R R2
U 1 1 5D6666C3
P 4150 2550
F 0 "R2" V 4225 2500 50  0000 L CNN
F 1 "1K5" V 4050 2475 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4080 2550 50  0001 C CNN
F 3 "~" H 4150 2550 50  0001 C CNN
	1    4150 2550
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D2
U 1 1 5D6666CA
P 4550 2550
F 0 "D2" H 4600 2650 50  0000 R CNN
F 1 "RED LED" H 4800 2450 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric" H 4550 2550 50  0001 C CNN
F 3 "~" H 4550 2550 50  0001 C CNN
	1    4550 2550
	1    0    0    -1  
$EndComp
$Comp
L VeinCam_Symbols:SFH7252 D3
U 1 1 5C89C23B
P 6600 1800
F 0 "D3" H 6600 2050 50  0000 C CNN
F 1 "SFH7252" H 6600 1550 50  0000 C CNN
F 2 "VeinCam_Footprints:SFH7252" H 6630 1800 50  0001 C CNN
F 3 "~" H 6630 1800 50  0001 C CNN
	1    6600 1800
	1    0    0    -1  
$EndComp
$Comp
L VeinCam_Symbols:SFH7252 D4
U 1 1 5C89C451
P 6600 2450
F 0 "D4" H 6600 2700 50  0000 C CNN
F 1 "SFH7252" H 6600 2200 50  0000 C CNN
F 2 "VeinCam_Footprints:SFH7252" H 6630 2450 50  0001 C CNN
F 3 "~" H 6630 2450 50  0001 C CNN
	1    6600 2450
	1    0    0    -1  
$EndComp
$Comp
L VeinCam_Symbols:SFH7252 D6
U 1 1 5C89C4E7
P 7550 2450
F 0 "D6" H 7550 2700 50  0000 C CNN
F 1 "SFH7252" H 7550 2200 50  0000 C CNN
F 2 "VeinCam_Footprints:SFH7252" H 7580 2450 50  0001 C CNN
F 3 "~" H 7580 2450 50  0001 C CNN
	1    7550 2450
	1    0    0    -1  
$EndComp
$Comp
L VeinCam_Symbols:SFH7252 D8
U 1 1 5C89C583
P 8500 2450
F 0 "D8" H 8500 2700 50  0000 C CNN
F 1 "SFH7252" H 8500 2200 50  0000 C CNN
F 2 "VeinCam_Footprints:SFH7252" H 8530 2450 50  0001 C CNN
F 3 "~" H 8530 2450 50  0001 C CNN
	1    8500 2450
	1    0    0    -1  
$EndComp
$Comp
L VeinCam_Symbols:SFH7252 D7
U 1 1 5C89C61B
P 8500 1800
F 0 "D7" H 8500 2050 50  0000 C CNN
F 1 "SFH7252" H 8500 1550 50  0000 C CNN
F 2 "VeinCam_Footprints:SFH7252" H 8530 1800 50  0001 C CNN
F 3 "~" H 8530 1800 50  0001 C CNN
	1    8500 1800
	1    0    0    -1  
$EndComp
$Comp
L VeinCam_Symbols:SFH7252 D5
U 1 1 5C89C6B9
P 7550 1800
F 0 "D5" H 7550 2050 50  0000 C CNN
F 1 "SFH7252" H 7550 1550 50  0000 C CNN
F 2 "VeinCam_Footprints:SFH7252" H 7580 1800 50  0001 C CNN
F 3 "~" H 7580 1800 50  0001 C CNN
	1    7550 1800
	1    0    0    -1  
$EndComp
NoConn ~ 1050 1750
NoConn ~ 1050 1950
NoConn ~ 1050 2050
NoConn ~ 1050 2450
NoConn ~ 1050 2550
NoConn ~ 1050 2950
NoConn ~ 1050 3050
NoConn ~ 1050 3250
NoConn ~ 2650 3050
NoConn ~ 2650 2950
NoConn ~ 2650 2850
NoConn ~ 2650 2750
NoConn ~ 2650 2650
NoConn ~ 2650 2450
NoConn ~ 2650 2350
$Comp
L power:PWR_FLAG #FLG01
U 1 1 5C8B7FB3
P 850 7500
F 0 "#FLG01" H 850 7575 50  0001 C CNN
F 1 "PWR_FLAG" H 850 7674 50  0000 C CNN
F 2 "" H 850 7500 50  0001 C CNN
F 3 "~" H 850 7500 50  0001 C CNN
	1    850  7500
	-1   0    0    1   
$EndComp
Wire Wire Line
	850  7500 850  7450
$Comp
L power:+3V3 #PWR01
U 1 1 5C906036
P 850 7450
F 0 "#PWR01" H 850 7300 50  0001 C CNN
F 1 "+3V3" H 865 7623 50  0000 C CNN
F 2 "" H 850 7450 50  0001 C CNN
F 3 "" H 850 7450 50  0001 C CNN
	1    850  7450
	1    0    0    -1  
$EndComp
NoConn ~ 1050 2850
NoConn ~ 2650 3250
NoConn ~ 12400 3300
NoConn ~ 1050 2750
Text Notes 750  6300 0    100  ~ 0
For Camera
$Comp
L Connector:TestPoint TP1
U 1 1 5C93105D
P 850 6500
F 0 "TP1" H 908 6620 50  0000 L CNN
F 1 "Camera Outline" H 908 6529 50  0000 L CNN
F 2 "VeinCam_Footprints:PiCamera" H 1050 6500 50  0001 C CNN
F 3 "~" H 1050 6500 50  0001 C CNN
	1    850  6500
	1    0    0    -1  
$EndComp
NoConn ~ 850  6500
NoConn ~ 2650 1950
NoConn ~ 2650 2050
$Comp
L VeinCam_Symbols:NTJD4001N Q1
U 1 1 5C91E58D
P 8900 2950
F 0 "Q1" H 9106 2996 50  0000 L CNN
F 1 "NTJD4001N" H 9106 2905 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-363_SC-70-6" H 9100 2950 50  0001 C CNN
F 3 "~" H 9100 2950 50  0001 C CNN
	1    8900 2950
	1    0    0    -1  
$EndComp
$Comp
L VeinCam_Symbols:NTJD4001N Q1
U 2 1 5C91E612
P 10350 2950
F 0 "Q1" H 10556 2996 50  0000 L CNN
F 1 "NTJD4001N" H 10556 2905 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-363_SC-70-6" H 10550 2950 50  0001 C CNN
F 3 "~" H 10550 2950 50  0001 C CNN
	2    10350 2950
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0101
U 1 1 5CB9F567
P 2050 1150
F 0 "#PWR0101" H 2050 1000 50  0001 C CNN
F 1 "+3V3" H 2065 1323 50  0000 C CNN
F 2 "" H 2050 1150 50  0001 C CNN
F 3 "" H 2050 1150 50  0001 C CNN
	1    2050 1150
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0103
U 1 1 5CBA5562
P 4900 2500
F 0 "#PWR0103" H 4900 2350 50  0001 C CNN
F 1 "+3V3" H 4915 2673 50  0000 C CNN
F 2 "" H 4900 2500 50  0001 C CNN
F 3 "" H 4900 2500 50  0001 C CNN
	1    4900 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 2500 4900 2550
Wire Wire Line
	4700 2550 4900 2550
Wire Wire Line
	4700 1900 4900 1900
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 5D30B49A
P 1850 2550
F 0 "J1" H 1200 3900 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 1250 3800 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 1850 2550 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 1850 2550 50  0001 C CNN
	1    1850 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 1150 2050 1250
NoConn ~ 1950 1250
$Comp
L power:GND #PWR0102
U 1 1 5CC02B04
P 4900 1950
F 0 "#PWR0102" H 4900 1700 50  0001 C CNN
F 1 "GND" H 4905 1777 50  0000 C CNN
F 2 "" H 4900 1950 50  0001 C CNN
F 3 "" H 4900 1950 50  0001 C CNN
	1    4900 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 1900 4900 1950
Wire Wire Line
	3500 1900 4000 1900
Wire Wire Line
	4300 1900 4400 1900
NoConn ~ 1050 1650
NoConn ~ 2650 2250
Wire Wire Line
	3500 2550 4000 2550
Wire Wire Line
	4300 2550 4400 2550
Wire Wire Line
	5550 2250 5500 2250
Wire Wire Line
	5500 2250 5500 2150
Wire Wire Line
	5500 1950 5550 1950
Wire Wire Line
	5550 2050 5500 2050
Connection ~ 5500 2050
Wire Wire Line
	5500 2050 5500 1950
Wire Wire Line
	5550 2150 5500 2150
Connection ~ 5500 2150
Wire Wire Line
	5500 2150 5500 2050
Wire Wire Line
	5500 1750 5500 1950
Connection ~ 5500 1950
Wire Wire Line
	6050 1700 6300 1700
$Comp
L Device:R_Pack04 RN1
U 1 1 5CEA12D3
P 5750 2150
F 0 "RN1" V 5333 2150 50  0000 C CNN
F 1 "R_Pack_3R3" V 5424 2150 50  0000 C CNN
F 2 "Resistor_SMD:R_Array_Convex_4x0603" V 6025 2150 50  0001 C CNN
F 3 "~" H 5750 2150 50  0001 C CNN
	1    5750 2150
	0    1    1    0   
$EndComp
Wire Wire Line
	5950 2250 6150 2250
Wire Wire Line
	6150 2250 6150 2350
Wire Wire Line
	6150 2350 6300 2350
Wire Wire Line
	6050 2550 6050 2150
Wire Wire Line
	6050 2150 5950 2150
Wire Wire Line
	6050 2550 6300 2550
Wire Wire Line
	5950 1950 6050 1950
Wire Wire Line
	6050 1950 6050 1700
Wire Wire Line
	6150 2050 6150 1900
Wire Wire Line
	6150 1900 6300 1900
Wire Wire Line
	5950 2050 6150 2050
$EndSCHEMATC