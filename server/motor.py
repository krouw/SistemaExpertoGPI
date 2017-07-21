def fuzzyLogic(body):
	Hacone = []
	FactBio=[]
	FactAmb=[]
	HCN=0
	FA=0
	FB=0
	contador = 0
	Total = 0

	for i in range(1,3):
		pregunta = float(body[i])
		FactBio.append(pregunta)
		FB = FB+pregunta
		contador = contador + 1
		#print pregunta

	for i in range(3,5):
		pregunta = float(body[i])
		FactAmb.append(pregunta)
		FA = FA+pregunta
		contador = contador + 1
		#print pregunta

	for i in range(5,32):
		pregunta = float(body[i])
		Hacone.append(pregunta)
		HCN = HCN+pregunta
		contador = contador + 1
		#print pregunta

	Total=FB+FA+HCN
	print contador
	print Total

	cargouni = { 'presidente':4057099, 'vicepresidente':4057095, 'asesor financiero':4057086, 'jefe de proyecto':4027088, 'jefe de departamentos':4057086, 'subjefe de departamentos':4027085, 'auditor':4026081, 'contador':4026083, 'medico general':4026075, 'medico especialista':4026077, 'coordinador':4027076 }
	cargotec = { 'ayudante mantenimiento':3000060, 'despachador farmacia':3015659, 'secretaria':3010658, 'enfermera':3000073 }
	cargomedia = { 'aseo':43, 'guardia':52 }

	result = []

	if Total >= 4027076:
		for k,v in cargouni.iteritems():
			if Total >= v:
				result.append(k)
	elif Total >= 3000060:
		for k,v in cargotec.iteritems():
			if Total>=v:
				result.append(k)
	elif Total < 3000000:
		for k,v in cargomedia.iteritems():
			if Total>=v:
				result.append(k)
	return result
