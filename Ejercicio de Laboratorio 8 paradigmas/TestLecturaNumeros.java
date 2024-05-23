import java.io.IOException;

public class TestLecturaNumeros {

    public static void main(String[] args) {
        try {
            LecturaNumeros lector = new LecturaNumeros();
            
            System.out.println("Introduce 5 números:");

            int numero1 = lector.readInt("Introduce un número entero: ");
            int numero2 = lector.readInt("Introduce otro número entero: ");
            Integer numero3 = lector.readInteger(); // Corrección aquí
            double numero4 = lector.readDouble("Introduce un número decimal: ");
            Double numero5 = lector.readDouble("Introduce un número decimal (en forma de Double): ");

            System.out.println("Los números introducidos son:");
            System.out.println("Número entero 1: " + numero1);
            System.out.println("Número entero 2: " + numero2);
            System.out.println("Número entero (en forma de Integer): " + numero3);
            System.out.println("Número decimal: " + numero4);
            System.out.println("Número decimal (en forma de Double): " + numero5);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
