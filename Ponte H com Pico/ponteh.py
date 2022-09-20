import machine                            #|   #include "Arduino.h"
import utime                              #|
                                          #|   void setup() {
                                          #|      Serial.begin(9600);
frenteEsq = machine.PWM(machine.Pin(2))   #|      pinMode(2, OUTPUT); 
trasEsq   = machine.PWM(machine.Pin(3))   #|      pinMode(3, OUTPUT);
                                          #|
frenteDir = machine.PWM(machine.Pin(4))   #|      pinMode(4, OUTPUT);
trasDir   = machine.PWM(machine.Pin(5))   #|      pinMode(5, OUTPUT);
                                          #|   
frenteEsq.freq(1000);                     #|      pararMotores();   
trasEsq.freq(1000);                       #|      delay(2000);
frenteDir.freq(1000);                     #|      Serial.println("Inicio do Loop")
trasDir.freq(1000);                       #|   }
                                          #|
def pararMotores():                       #|   void pararMotores() {
    frenteEsq.duty_u16(0)                 #|      analogWrite(2, LOW);
    trasEsq.duty_u16(0)                   #|      analogWrite(3, LOW);
    frenteDir.duty_u16(0)                 #|      analogWrite(4, LOW);
    trasDir.duty_u16(0)                   #|      analogWrite(5, LOW);
                                          #|   }
pararMotores()                            #|
utime.sleep(2)                            #|
                                          #|
print("Inicio do loop")                   #|
                                          #|
while True:                               #|   void loop() {
    print("Frente")                       #|      Serial.print("Frente"); 
    # MOVER PARA FRENTE                   #|
    frenteEsq.duty_u16(23000)             #|      analogWrite(2, 127);
    trasEsq.duty_u16(0)                   #|      analogWrite(3, 0);
    frenteDir.duty_u16(23000)             #|      analogWrite(4, 127);
    trasDir.duty_u16(0)                   #|      analogWrite(5, 0);
    utime.sleep(1)                        #|      delay(1000);
                                          #|    
    # PARAR OS MOTORES                    #|
    pararMotores()                        #|      pararMotores();
    utime.sleep(1)                        #|      delay(1000);
                                          #|    
    print("Tras")                         #|      Serial.print("Tras");
    # MOVER PARA TRAS                     #|
    frenteEsq.duty_u16(0)                 #|      analogWrite(2, 0);
    trasEsq.duty_u16(23000)               #|      analogWrite(3, 127);
    frenteDir.duty_u16(0)                 #|      analogWrite(4, 0);
    trasDir.duty_u16(23000)               #|      analogWrite(5, 127);
    utime.sleep(1)                        #|      delay(1000);
                                          #|    
    # PARAR OS MOTORES                    #|
    pararMotores()                        #|      pararMotores();
    utime.sleep(1)                        #|      delay(1000);
                                          #|    
    print("Esquerda")                     #|      Serial.print("Esquerda");
    # GIRAR PARA ESQUERDA                 #|
    frenteEsq.duty_u16(0)                 #|      analogWrite(2, 0);
    trasEsq.duty_u16(23000)               #|      analogWrite(3, 127);
    frenteDir.duty_u16(23000)             #|      analogWrite(4, 127);
    trasDir.duty_u16(0)                   #|      analogWrite(5, 0);
    utime.sleep(1)                        #|      delay(1000);
                                          #|    
    # PARAR OS MOTORES                    #|
    pararMotores()                        #|      pararMotores();
    utime.sleep(1)                        #|      delay(1000);
                                          #|    
    print("Direita")                      #|      Serial.print("Direita");
    # GIRAR PARA DIREITA                  #|
    frenteEsq.duty_u16(23000)             #|      analogWrite(2, 127);
    trasEsq.duty_u16(0)                   #|      analogWrite(3, 0);
    frenteDir.duty_u16(0)                 #|      analogWrite(4, 0);
    trasDir.duty_u16(23000)               #|      analogWrite(5, 127);
    utime.sleep(1)                        #|      delay(1000);
                                          #|    
    # PARAR OS MOTORES                    #|
    pararMotores()                        #|      pararMotores();
    utime.sleep(1)                        #|      delay(1000);