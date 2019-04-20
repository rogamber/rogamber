#include <SPI.h>
#include <Ethernet.h>

// MAC address from Ethernet shield sticker under board
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(10, 0, 0, 50); // IP address, may need to change depending on network
EthernetServer server(80);  // create a server at port 80

int req_index = 0; // index para captura de Peticion
char c="";
String peticion = "";
const int s1 = 3;//de define Dispositivo 1 en salida Digital #3
const int s2 = 4;//de define Dispositivo 1 en salida Digital #4
bool s3=0;
bool s4=0;
bool s5=0;
bool estado[4];

void setup()
{
    pinMode(10, OUTPUT);
    digitalWrite(10, HIGH);// disable Ethernet chip
    pinMode(s1, OUTPUT);
    digitalWrite(s1,LOW);
    pinMode(s2, OUTPUT);
    digitalWrite(s2,LOW);
    
    Serial.begin(9600);       // for debugging
        
    Ethernet.begin(mac, ip);  // initialize Ethernet device
    server.begin();           // start to listen for clients
}

bool sensor1()
{
  return 0;
}
void loop()
{
    EthernetClient client = server.available();  // try to get client
    req_index = 0;
    peticion = "";
    if (client) {  // got client?
        client.println("HTTP/1.1 200 OK"); // Enviar una respuesta tipica
        client.println("Content-Type: text/html");
        client.println("Connection: close");  
        client.println();
        //Inicio Pagina Web
        client.println("<!DOCTYPE HTML>");
        client.println("<html>");
        client.println("<head>");
        client.println("<title>ROGAMBER Servidor Arduino</title>");
        client.println("<META HTTP-EQUIV='REFRESH' CONTENT='1;URL=http://179.50.133.204'> ");//Refresca cada 1 segundo y redirige a la Pagina Inicial
        client.println("<style type='text/css'>");
        client.println("h1 {font-family: courier, courier-new, serif;font-size: 20pt;color:#FFFFFF;border-bottom: 2px solid blue;}");
        client.println("p {font-family: arial, verdana, sans-serif;font-size: 35pt;color: #B72F11;}");
        client.println("a {font-family: arial, verdana, sans-serif;font-size: 35pt;color: #FFFFFF;}");
        client.println("body {color:#FFFFFF;background-color:#0072C6;margin:0;}");
        client.println(".red_txt {color: red;}");
        client.println("</style>");
        client.println("</head>");
        client.println("<body>");
        client.println("<h1>ROGAMBER Servidor Arduino</h1>");
        estado[0] = digitalRead(s1);
        if (estado[0] == LOW){
           client.println("<p>Encender <a href='accion01'>Dispositivo 1</a></p>");
                    }
        else {
           client.println("<p>Apagar <a href='accion01'>Dispositivo 1</a></p>");
             }
        estado[1] = digitalRead(s2);
        if (estado[1] == LOW){
           client.println("<p>Encender <a href='accion02'>Dispositivo 2</a></p>");
                    }
        else {
           client.println("<p>Apagar <a href='accion02'>Dispositivo 2</a></p>");
             }         
        if (s3 == 0){
           client.println("<p>Encender <a href='accion03'>Dispositivo 3</a></p>");
                    }
        else {
           client.println("<p>Apagar <a href='accion03'>Dispositivo 3</a></p>");
             }  
        if (s4 == 0){
           client.println("<p>Encender <a href='accion04'>Dispositivo 4</a></p>");
                    }
        else {
           client.println("<p>Apagar <a href='accion04'>Dispositivo 4</a></p>");
             }  
        if (s5 == 0){
           client.println("<p>Encender <a href='accion05'>Dispositivo 5</a></p>");
                    }
        else {
           client.println("<p>Apagar <a href='accion05'>Dispositivo 5</a></p>");
             }  
        client.println("</body>");
        client.println("</html>");
        //Final Pagina Web                                                       
               
        while (client.connected()) {
            if (client.available()) {  // client data available to read
                char c = client.read(); // read 1 byte (character) from client
                                
                if (c != '\n' && req_index < 13){
                   peticion = peticion+c;
                              }
                req_index++;
                if (c == '\n') {
                   if (peticion == "GET /accion01"){
                     
                      if (estado[0]==LOW){
                          digitalWrite(s1,HIGH); 
                                }
                      else {
                             digitalWrite(s1,LOW);
                           }         
                      
                      } 
                   if (peticion == "GET /accion02"){
                            if (estado[1]==LOW){
                                digitalWrite(s2,HIGH);  
                                      }
                            else {
                                digitalWrite(s2,LOW);   
                                 }         
                      
                                                } 
                       
                   if (peticion == "GET /accion03"){
                            if (s3==0){
                               s3=1; 
                                }
                            else {
                               s3=0; 
                                 }         
                                                  } 
                   if (peticion == "GET /accion04"){
                            if (s4==0){
                               s4=1; 
                                }
                            else {
                               s4=0; 
                                 }         
                                                  } 
                   if (peticion == "GET /accion05"){
                           if (s5==0){
                                 s5=1; 
                                }
                           else {
                               s5=0; 
                                }         
                                                  }                           
                  
                   client.stop();   
                } 
                 
            } // end if (client.available())
        } // end while (client.connected())
     delay(1);      // give the web browser time to receive the data
      
    } // end if (client)
}//end loop
