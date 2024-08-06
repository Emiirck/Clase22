


fecha = input(print("Ingrese la fecha con el siguiente formato dia, mes año"))
meses = {
'Enero' : 1,
'Febrero' : 2,
'Marzo' : 3,
'Abril' : 4,
'Mayo' : 5,
'Junio' : 6,
'Julio' : 7,
'Agosto' : 8,
'Septiembre' : 9,
'Octubre' : 10,
'Nomviembre' : 11,
'Diciembre' : 12,
}

dia, mes_año = fecha.split(', ')
mes, año = mes_año.split('')
mes_numero = meses[mes]

print


