import broadlink
import time, os

devices = broadlink.S1C(host=("192.168.0.62",80), mac=bytearray.fromhex("34EA34F0BAA0")) # Change to your S1C IP Address and S1C Mac Address
devices.auth()

sens = devices.get_sensors_status()
old = sens


while 1:
	try:
		sens = devices.get_sensors_status()
		for i, se in enumerate(sens['sensors']):
			if se['status'] != old['sensors'][i]['status']:
				sName = se['name']
				sType = se['type']
				if sType == "Door Sensor" and str(se['status']) == "0" or sType == "Door Sensor" and str(se['status']) == "128": # Instead of sType you can test for sName in case you have multiple sensors
					print time.ctime() + ": Door closed: " + str(se['status'])
					os.system("mosquitto_pub -h 192.168.0.41 -p 1883 -t 'sensors/s1c/entrance_door' -u emaus -P arizinho -m " + "Fechada") # change the ip address, user name and password for your mosquitto server
				elif sType == "Door Sensor" and str(se['status']) == "16" or sType == "Door Sensor" and str(se['status']) == "144":
					print time.ctime()  +": Door opened: " + str(se['status'])
					os.system("mosquitto_pub -h 192.168.0.41 -p 1883 -t 'sensors/s1c/entrance_door' -u emaus -P arizinho -m " + "Aberta")
				elif sType == "Door Sensor" and str(se['status']) == "48":
					print time.ctime()  +": Door Sensor tampered: " + str(se['status'])
					os.system("mosquitto_pub -h 192.168.0.41 -p 1883 -t 'sensors/s1c/entrance_door' -u emaus -P arizinho -m " + "Irregular")
				elif sType == "Motion Sensor" and str(se['status']) == "0" or sType == "Motion Sensor" and str(se['status']) == "128":
					print time.ctime()  +": No Motion: " + str(se['status'])
					os.system("mosquitto_pub -h 192.168.0.41 -p 1883 -t 'sensors/s1c/motion_sensor' -u emaus -P arizinho -m " + "Sem_movimento")
				elif sType == "Motion Sensor" and str(se['status']) == "16":
					print time.ctime()  +": Motion Detected: " + str(se['status'])
					os.system("mosquitto_pub -h 192.168.0.41 -p 1883 -t 'sensors/s1c/motion_sensor' -u emaus -P arizinho -m " + "Movimento_detectado")
				elif sType == "Motion Sensor" and str(se['status']) == "32":
					print time.ctime()  +": Motion Sensor Tampered: " + str(se['status'])
					os.system("mosquitto_pub -h 192.168.0.41 -p 1883 -t 'sensors/s1c/motion_sensor' -u emaus -P arizinho -m " + "Irregular")
				old = sens
	except:
		continue
