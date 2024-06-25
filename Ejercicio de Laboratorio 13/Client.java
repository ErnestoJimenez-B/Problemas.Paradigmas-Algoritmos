import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client {
    public static void main(String[] args) {
        String hostName = "localhost"; // Dirección del servidor, localhost significa que está en la misma máquina
        int port = 5000; // El puerto debe coincidir con el que el servidor está escuchando

        try (Socket socket = new Socket(hostName, port); // Crear un socket conectado al servidor
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true); // Stream para enviar datos al servidor
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) { // Stream para recibir datos del servidor

            // Enviar mensaje al servidor
            out.println("Hola, servidor!"); // Enviar un mensaje al servidor
            System.out.println("Mensaje enviado al servidor."); // Confirmación en la consola del cliente

            // Leer la respuesta del servidor
            String respuesta = in.readLine(); // Leer la respuesta enviada por el servidor
            System.out.println("Respuesta del servidor: " + respuesta); // Mostrar la respuesta en la consola del cliente

        } catch (UnknownHostException e) { // Manejar error si el host es desconocido
            System.out.println("No se pudo detectar el servidor en " + hostName); // Mensaje de error
            System.out.println(e.getMessage()); // Mostrar detalles del error
        } catch (IOException e) { // Manejar error de entrada/salida
            System.out.println("No se pudo obtener I/O para la conexión con: " + hostName); // Mensaje de error
            System.out.println(e.getMessage()); // Mostrar detalles del error
        }
    }
}
