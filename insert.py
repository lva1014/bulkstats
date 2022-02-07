#!/usr/bin/python

import datetime, sys, re

def calc_stamp(date1,time1):
	"""
	Description goes here
	"""
	try:
		year	= date1[:4]
		month	= date1[4:6]
		day		= date1[6:8]
		hour	= time1[:2]
		min		= time1[2:4]
		sec		= time1[4:6]
		
		t = datetime.datetime(int(year),int(month),int(day),int(hour),int(min),int(sec))
		timestamp = (t-datetime.datetime(1970,1,1)).total_seconds()
	except:
		timestamp = None
	timestamp = int(timestamp)	
	return str(timestamp)+'000000000'


def check_err(val):
	"""
	Decscription goes here
	"""
	#val = val.replace("%","")
	#val = val.replace(".","_")
	if re.search(r'^%',val):
		return -1
	if re.search(r'[a-z]',val):
		return -1
	if re.search(r'[A-Z]',val):
		return -1
	if val.count(".")>1:
		return -1
	if val.count(":")>=1:
		return -1
	if val.count(";")>=1:
		return -1
	return val
	
	
def check_err2(val):
	"""
	Decscription goes here
	"""
	val = val.replace(" ","_")
	return val
	

def go_insert(name,conf_line,line,node):
	"""
	Decscription goes here
	"""
	try:
		#
		if re.search(r'^Card[0-9]{0,1}$',name):
			# EMS,Card<n>,%localdate%,%localtime%,%card%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			card = line_[4]
			val1 = (conf_line.split(","))[5:]
			val2 = line_[5:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """card,node=%s,card=%s %s %s""" %(node,card,ins_vals,timestamp)
			
			return sql

		# temporary fix!
		if re.search(r'^Car[0-9]{1,1}$',name):
			# EMS,Card<n>,%localdate%,%localtime%,%card%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			card = line_[4]
			val1 = (conf_line.split(","))[5:]
			val2 = line_[5:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """card,node=%s,card=%s %s %s""" %(node,card,ins_vals,timestamp)
			
			return sql


		#
		if re.search(r'^Port$',name):
			# EMS,Port,%localdate%,%localtime%,%card%,%port%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			card = line_[4]
			port = line_[5]
			val1 = (conf_line.split(","))[6:]
			val2 = line_[6:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """port,node=%s,card=%s,port=%s %s %s""" %(node,card,port,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^PDSNSystem[\w]{0,1}$',name):
			# EMS,PDSNSystem<n>,%localdate%,%localtime%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			val1 = (conf_line.split(","))[4:]
			val2 = line_[4:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """system,node=%s %s %s""" %(node,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^PPP[0-9]{1}$',name):
			# EMS,PPP<n>,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	  = line_[4]
			vpnid	  = line_[5]
			servname  = line_[6]
			val1 = (conf_line.split(","))[7:]
			val2 = line_[7:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """ppp,node=%s,vpnname=%s,vpnid=%s,servname=%s %s %s""" %(node,vpnname,vpnid,servname,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^GTPC[0-9]{1}$',name):
			# EMS,GTPC<n>,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	  = line_[4]
			vpnid	  = line_[5]
			servname  = line_[6]
			val1 = (conf_line.split(","))[7:]
			val2 = line_[7:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """gtpc,node=%s,vpnname=%s,vpnid=%s,servname=%s %s %s""" %(node,vpnname,vpnid,servname,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^GTPP[0-9]{0,1}$',name):
			# EMS,GTPP,%localdate%,%localtime%,%vpnname%,%vpnid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	  = line_[4]
			vpnid	  = line_[5]
			servname  = line_[6]
			val1 = (conf_line.split(","))[7:]
			val2 = line_[7:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """gtpp,node=%s,vpnname=%s,vpnid=%s %s %s""" %(node,vpnname,vpnid,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^IPPOOL$',name):
			# EMS,IPPOOL,%localdate%,%localtime%,%vpnname%,%vpnid%,%name%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	  = line_[4]
			vpnid	  = line_[5]
			name  	  = line_[6]
			val1 = (conf_line.split(","))[7:]
			val2 = line_[7:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """ippool,node=%s,vpnname=%s,vpnid=%s,name=%s %s %s""" %(node,vpnname,vpnid,name,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^APN[0-9]{0,1}$',name):
			# EMS,APN,%localdate%,%localtime%,%vpnname%,%vpnid%,%apn%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	  = line_[4]
			vpnid	  = line_[5]
			apn  	  = line_[6]
			val1 = (conf_line.split(","))[7:]
			val2 = line_[7:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """apn,node=%s,vpnname=%s,vpnid=%s,apn=%s %s %s""" %(node,vpnname,vpnid,apn,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^DIAMETERAUTH1$',name):
			# EMS,DIAMETERAUTH1,%localdate%,%localtime%,%vpnname%,%vpnid%,%servertype%,%group%,%ipaddr%,%port%,%peer%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	    = line_[4]
			vpnid	    = line_[5]
			servertype  = line_[6]
			group		= line_[7]
			ipaddr		= line_[8]
			port		= line_[9]
			peer		= line_[10]
			val1 = (conf_line.split(","))[11:]
			val2 = line_[11:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """diameter-auth,node=%s,vpnname=%s,vpnid=%s,servertype=%s,group=%s,ipaddr=%s,port=%s,peer=%s %s %s""" %(node,vpnname,vpnid,servertype,group,ipaddr,port,peer,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^DIAMETERACCT1$',name):
			# EMS,DIAMETERACCT1,%localdate%,%localtime%,%vpnname%,%vpnid%,%servertype%,%group%,%ipaddr%,%port%,%peer%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	    = line_[4]
			vpnid	    = line_[5]
			servertype  = line_[6]
			group		= line_[7]
			ipaddr		= line_[8]
			port		= line_[9]
			peer		= line_[10]
			val1 = (conf_line.split(","))[11:]
			val2 = line_[11:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """diameter-acct,node=%s,vpnname=%s,vpnid=%s,servertype=%s,group=%s,ipaddr=%s,port=%s,peer=%s %s %s""" %(node,vpnname,vpnid,servertype,group,ipaddr,port,peer,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^ECS[\w]{1}$',name):
			# EMS,ECS1,%localdate%,%localtime%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			val1 = (conf_line.split(","))[4:]
			val2 = line_[4:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """ecs,node=%s %s %s""" %(node,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^DCCAGroup[0-9]{1}$',name):
			# EMS,DCCAGroup1,%localdate%,%localtime%,%acs-service%,%cc-group%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			acs_service	 = line_[4]
			cc_group	 = line_[5]
			if cc_group.count(" ")>0:
				cc_group = "Unknown"
			val1 = (conf_line.split(","))[6:]
			val2 = line_[6:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
			else:
				print "arrays are not equal!"
			ins_vals = ",".join(ins_vals)
			sql = """dcca-group,node=%s,acs-service=%s,cc-group=%s %s %s""" %(node,acs_service,cc_group,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^CONTEXT[0-9]{0,1}$',name):
			# EMS,CONTEXT,%localdate%,%localtime%,%vpnname%,%vpnid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			val1 = (conf_line.split(","))[6:]
			val2 = line_[6:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """context,node=%s,vpnname=%s,vpnid=%s %s %s""" %(node,vpnname,vpnid,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^EGTPC[0-9A-Z]{1}$',name):
			# EMS,EGTPC1,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servname = line_[6]
			servid	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """egtpc,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^IMSA[0-9]{0,1}$',name):
			# EMS,IMSA,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servname = line_[6]
			servid	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """imsa,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^PGW[0-9A-Z]{1}$',name):
			# EMS,PGW1,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servname = line_[6]
			servid	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """pgw,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^SGW.$',name):
			# EMS,SGW1,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servname = line_[6]
			servid	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """sgw,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^DPCA[0-9]{1}$',name):
			# EMS,DPCA1,%localdate%,%localtime%,%vpnname%,%vpnid%,%ipaddr%,%port%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			ipaddr = line_[6]
			port	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """dpca,node=%s,vpnname=%s,vpnid=%s,ipaddr=%s,port=%s %s %s""" %(node,vpnname,vpnid,ipaddr,port,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^DCCA1$',name):
			# EMS,DCCA1,%localdate%,%localtime%,%vpnname%,%vpnid%,%ipaddr%,%port%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			ipaddr = line_[6]
			port	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """dcca,node=%s,vpnname=%s,vpnid=%s,ipaddr=%s,port=%s %s %s""" %(node,vpnname,vpnid,ipaddr,port,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^DCCA2$',name):
			# EMS,DCCA2,%localdate%,%localtime%,%vpnname%,%vpnid%,%ipaddr%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			ipaddr = line_[6]
			val1 = (conf_line.split(","))[7:]
			val2 = line_[7:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """dcca,node=%s,vpnname=%s,vpnid=%s,ipaddr=%s %s %s""" %(node,vpnname,vpnid,ipaddr,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^GTPU[0-9]{1}$',name):
			# EMS,GTPU1,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servname = line_[6]
			servid	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1 
				
			ins_vals = ",".join(ins_vals)
			sql = """gtpu,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^VLAN.NPU[0-9]{0,1}$',name):
			# EMS,VLAN_NPU,%localdate%,%localtime%,%vpnname%,%vpnid%,%port-no%,%slot-no%,%interfacename%,%interface%,%interfacetype%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			port_no = line_[6]
			slot_no	= line_[7]
			interfacename = line_[8]
			interface = line_[9]
			interfacetype = line_[10]
			val1 = (conf_line.split(","))[11:]
			val2 = line_[11:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """vlan-npu,node=%s,vpnname=%s,vpnid=%s,port-no=%s,slot-no=%s,interfacename=%s,interface=%s,interfacetype=%s %s %s""" %(node,vpnname,vpnid,port_no,slot_no,interfacename,interface,interfacetype,ins_vals,timestamp)		
			return sql
		#
		if re.search(r'^DIAMETER1$',name):
			# EMS,DIAMETER1,%localdate%,%localtime%,%endpoint-name%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			endpoint_name = line_[4]
			if endpoint_name.count(" ")>0:
				endpoint_name = endpoint_name.replace(" ","_")
			val1 = (conf_line.split(","))[5:]
			val2 = line_[5:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """diameter,node=%s,endpoint_name=%s %s %s""" %(node,endpoint_name,ins_vals,timestamp)		
			return sql
		
		if re.search(r'^SAMOG[0-9]{1}$',name):
			# EMS,SAMOG<n>,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servname = line_[6]
			servid	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """samog,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql			
		
		#
		if re.search(r'^EPDG[0-9]{1,1}$',name):
			# EMS,EPDG[n],%localdate%,%localtime%,%endpoint-name%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servname = line_[6]
			servid	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """epdg,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql			

		#
		if re.search(r'^samog',name):
			# EMS,samog,samogSch1,localdate,localtime,vpnname,vpnid,servname,servid,...
			line = line[:-1]
			conf_line = conf_line[:-1]
			line_ = line.split(",")
			timestamp = calc_stamp(line_[3],line_[4])
			vpnname	= line_[5]
			vpnid	= line_[6]
			servname = line_[7]
			servid	= line_[8]
			val1 = (conf_line.split(","))[9:]
			val2 = line_[9:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
			else:
				pass
				#print('arrays are not equal!',len(val1),len(val2))
			ins_vals = ",".join(ins_vals)
			sql = """samog,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql	

		# added on 11 July 2017
		#
		if re.search(r'^RADIUS',name):
			# EMS,RADIUS,%localdate%,%localtime%,%vpnname%,%vpnid%,%servertype%,%ipaddr%,...
			line = line[:-1]
			conf_line = conf_line[:-1]
			line_ = line.split(",")
			timestamp = calc_stamp(line_[3],line_[4])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servname = line_[6]
			ipaddr	= line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
			else:
				pass
				#print('arrays are not equal!',len(val1),len(val2))
			ins_vals = ",".join(ins_vals)
			sql = """radius,node=%s,vpnname=%s,vpnid=%s,servname=%s,ipaddr=%s %s %s""" %(node,vpnname,vpnid,servname,ipaddr,ins_vals,timestamp)		
			return sql				
			
		#
		if re.search(r'^RADIUSGroup',name):
			# EMS,RADIUSGroup,%localdate%,%localtime%,%vpnname%,%vpnid%,%servertype%,%ipaddr%,%nasipaddr%,%port%,%group%,...
			line = line[:-1]
			conf_line = conf_line[:-1]
			line_ = line.split(",")
			timestamp = calc_stamp(line_[3],line_[4])
			vpnname	= line_[4]
			vpnid	= line_[5]
			servertype = line_[6]
			ipaddr	= line_[7]
			nasipaddr	= line_[8]
			port	= line_[9]
			group	= line_[10]
			val1 = (conf_line.split(","))[11:]
			val2 = line_[11:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
			else:
				pass
				#print('arrays are not equal!',len(val1),len(val2))
			ins_vals = ",".join(ins_vals)
			sql = """radius-group,node=%s,vpnname=%s,vpnid=%s,servertype=%s,ipaddr=%s,nasipaddr=%s,port=%s,group=%s %s %s""" %(node,vpnname,vpnid,servertype,ipaddr,nasipaddr,port,group,ins_vals,timestamp)		
			return sql				

		#
		if re.search(r'^P2P[0-9]{1,1}$',name):
			# EMS,P2P1,%localdate%,%localtime%,%p2p-protocol%,...
			line = line[:-1]
			conf_line = conf_line[:-1]
			line_ = line.split(",")
			timestamp = calc_stamp(line_[3],line_[4])
			p2pprotocol	= line_[4]
			val1 = (conf_line.split(","))[5:]
			val2 = line_[5:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
			else:
				pass
				#print('arrays are not equal!',len(val1),len(val2))
			ins_vals = ",".join(ins_vals)
			sql = """p2p,node=%s,p2p-protocol=%s %s %s""" %(node,p2pprotocol,ins_vals,timestamp)		
			return sql				

		#
		if re.search(r'^VLAN_NPU[0-9]{0,1}$',name):
			# EMS,VLAN_NPU,%localdate%,%localtime%,%vpnname%,%vpnid%,%port-no%,%slot-no%,%interfacename%,%interface%,%interfacetype%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname = line_[4]
			vpnid = line_[5]
			portno = line_[6]
			slotno = line_[7]
			interfacename = line_[8]
			interface = line_[9]
			interfacetype = line_[10]
			val1 = (conf_line.split(","))[11:]
			val2 = line_[11:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """vlan-npu,node=%s,vpnname=%s,vpnid=%s,port-no=%s,slot-no=%s,interface-name=%s,interface=%s,interface-type=%s %s %s""" %(node,vpnname,vpnid,portno,slotno,interfacename,interface,interfacetype,ins_vals,timestamp)		
			return sql			

		#
		if re.search(r'^apn_qci[0-9]{0,1}$',name):
			# format EMS,apn_qci1,%localdate%,%localtime%,%apn%,%qci%,%vpnname%,%vpnid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			apn = line_[4]
			qci = line_[5]
			vpnname = line_[6]
			vpnid = line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """apn-qci,node=%s,apn=%s,qci=%s,vpnname=%s,vpnid=%s %s %s""" %(node,apn,qci,vpnname,vpnid,ins_vals,timestamp)		
			return sql	

		#
		if re.search(r'^pgw_egtpc_s5s8[0-9A-Z]{0,1}$',name):
			# format EMS,pgw_egtpc_s5s81,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname = line_[4]
			vpnid = line_[5]
			servname = line_[6]
			servid = line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """pgw-egtpc-s5s8,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql	

		#
		if re.search(r'^pgw_egtpc_s2a[0-9A-Z]{0,1}$',name):
			# format EMS,pgw_egtpc_s2a1,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname = line_[4]
			vpnid = line_[5]
			servname = line_[6]
			servid = line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """pgw-egtpc-s2a,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql	

		#
		if re.search(r'^pgw_egtpc_s2b[0-9A-Z]{0,1}$',name):
			# format EMS,pgw_egtpc_s2a1,%localdate%,%localtime%,%vpnname%,%vpnid%,%servname%,%servid%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname = line_[4]
			vpnid = line_[5]
			servname = line_[6]
			servid = line_[7]
			val1 = (conf_line.split(","))[8:]
			val2 = line_[8:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """pgw-egtpc-s2b,node=%s,vpnname=%s,vpnid=%s,servname=%s,servid=%s %s %s""" %(node,vpnname,vpnid,servname,servid,ins_vals,timestamp)		
			return sql				
			
			
		#
		if re.search(r'^flow_kpi[0-9A-Z]{0,1}$',name):
			# format EMS,flow_kpi1,%localdate%,%localtime%,%ecs-flow-rule-name%,...
			line_ = line.split(",")
			timestamp = calc_stamp(line_[2],line_[3])
			vpnname = line_[4]
			ecsflowrulename = line_[5]
			val1 = (conf_line.split(","))[6:]
			val2 = line_[6:]
			if len(val1) == len(val2):
				i = 0
				ins_vals = []
				while i < len(val1):
					val1_ = check_err2(val1[i])
					val2_ = check_err(val2[i])
					if val1_ and val2_:
						hola = str(val1_)+'='+str(val2_)
						ins_vals.append(hola)
					i += 1
				
			ins_vals = ",".join(ins_vals)
			sql = """flow-kpi,node=%s,ecs-flow-rule-name=%s %s %s""" %(node,ecsflowrulename,ins_vals,timestamp)		
			return sql
			
	except:	
		print('error in line: %s' %(line))
		print (sys.exc_info()[1])
