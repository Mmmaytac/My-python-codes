eded=int(input("ededi daxil edin"))
onaltiliq_eded=""
while eded>0:
    qaliq=eded%16
    if qaliq==15:
        onaltiliq_eded="F"+onaltiliq_eded
    elif qaliq==14:
        onaltiliq_eded = "E" + onaltiliq_eded
    elif qaliq==13:
        onaltiliq_eded = "D" + onaltiliq_eded
    elif qaliq==12:
        onaltiliq_eded = "C" + onaltiliq_eded
    elif qaliq==11:
        onaltiliq_eded = "B" + onaltiliq_eded
    elif qaliq==10:
        onaltiliq_eded = "A" + onaltiliq_eded
    else:
        onaltiliq_eded = str(qaliq) + onaltiliq_eded
    eded//=16
print(onaltiliq_eded)