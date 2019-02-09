def generate_text(passenger_name, flight_number, gate_number):
    a=passenger_name
    b=gate_number
    c=flight_number
    d= a+", go to gate "+str(b)+" for flight "+c+"."
    return d

e = generate_text("Sam Roger","AI221", 12)
print(e)





