public class Main {

    static class Persona {

        public String nombre;
        public int edad;
        public String direccion;
        public String telefono;
        public String correo;
        public String genero;
        public String ocupacion;
        public String nacionalidad;

        public Persona(String n) {
            nombre = n;
        }

        public Persona(String n, int e, String d, String t, String c, String g, String o, String na) {
            nombre = n;
            edad = e;
            direccion = d;
            telefono = t;
            correo = c;
            genero = g;
            ocupacion = o;
            nacionalidad = na;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String n) {
            nombre = n;
        }

        public int getEdad() {
            return edad;
        }

        public void setEdad(int e) {
            edad = e;
        }

        public String getDireccion() {
            return direccion;
        }

        public void setDireccion(String d) {
            direccion = d;
        }

        public String getTelefono() {
            return telefono;
        }

        public void setTelefono(String t) {
            telefono = t;
        }

        public String getCorreo() {
            return correo;
        }

        public void setCorreo(String c) {
            correo = c;
        }

        public String getGenero() {
            return genero;
        }

        public void setGenero(String g) {
            genero = g;
        }

        public String getOcupacion() {
            return ocupacion;
        }

        public void setOcupacion(String o) {
            ocupacion = o;
        }

        public String getNacionalidad() {
            return nacionalidad;
        }

        public void setNacionalidad(String na) {
            nacionalidad = na;
        }

        @Override
        public String toString() {
            return "Nombre: " + nombre + "\n" +
                   "Edad: " + edad + "\n" +
                   "Dirección: " + direccion + "\n" +
                   "Teléfono: " + telefono + "\n" +
                   "Correo: " + correo + "\n" +
                   "Género: " + genero + "\n" +
                   "Ocupación: " + ocupacion + "\n" +
                   "Nacionalidad: " + nacionalidad;
        }
    }

    public static void main(String[] args) {
        // Definición de los atributos
        String nombre = "Juan";
        int edad = 30;
        String direccion = "Calle Principal 123";
        String telefono = "123456789";
        String correo = "juan@example.com";
        String genero = "Masculino";
        String ocupacion = "Ingeniero";
        String nacionalidad = "Mexicana";

        // Creación de la instancia de Persona
        Persona persona1 = new Persona(nombre, edad, direccion, telefono, correo, genero, ocupacion, nacionalidad);

        // Impresión de los atributos
        System.out.println(persona1);
    }
}
