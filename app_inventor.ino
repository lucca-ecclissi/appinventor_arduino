//Variáveis 
int lumins = A0;
int led = 13;
char inChar = 'd';

//Informações iniciais 
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  Serial.available();//Esperando Informação da porta Serial
  inChar = (char)Serial.read();//Lendo informação
  if(inChar == 'd'){//Codição para acender led
    digitalWrite(led,LOW);
  }else if(inChar == 'l'){
    digitalWrite(led,HIGH);
  }
  Serial.print("s");//Enviando informações para a porta Serial
  Serial.print(analogRead(lumins));
  Serial.print("\n");
  delay(1000);
}
