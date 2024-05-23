import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;

public class LecturaNumeros extends BufferedReader {

    public LecturaNumeros() {
        super(new InputStreamReader(System.in));
    }

    public LecturaNumeros(Reader r) {
        super(r);
    }

    public int readInt() throws IOException {
        String input = this.readLine();
        return Integer.parseInt(input.trim());
    }

    public int readInt(String mensaje) throws IOException {
        System.out.print(mensaje);
        return this.readInt();
    }

    public Integer readInteger() throws IOException {
        return this.readInt();
    }

    public double readDouble() throws IOException {
        String input = this.readLine();
        return Double.parseDouble(input.trim());
    }

    public double readDouble(String mensaje) throws IOException {
        System.out.print(mensaje);
        return this.readDouble();
    }
}
