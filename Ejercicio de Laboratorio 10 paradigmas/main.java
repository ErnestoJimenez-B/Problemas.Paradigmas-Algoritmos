import java.lang.Math;
// clase abstracta figure , base para las figuras geometricas, con sus atributos como se hizo en python
abstract class Figure {
    String color;

    public Figure(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public abstract double perimeter();

    public abstract double area();
}
// Clase para el triangulo con sus atributos concretos
class Triangle extends Figure {
    double side1, side2, side3;

    public Triangle(String color, double side1, double side2, double side3) {
        super(color);
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    @Override
    public double perimeter() {
        return side1 + side2 + side3;
    }

    @Override
    public double area() {
        double s = (side1 + side2 + side3) / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }
}
// Clase para el circulo con sus atributos concretos
class Circle extends Figure {
    double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    @Override
    public double area() {
        return Math.PI * Math.pow(radius, 2);
    }
}
// Clase para el rectangulo con sus atributos concretos
class Rectangle extends Figure {
    double length, width;

    public Rectangle(String color, double length, double width) {
        super(color);
        this.length = length;
        this.width = width;
    }

    @Override
    public double perimeter() {
        return 2 * (length + width);
    }

    @Override
    public double area() {
        return length * width;
    }
}
// Clase para el hexagono con sus atributos concretos
class Hexagon extends Figure {
    double side;

    public Hexagon(String color, double side) {
        super(color);
        this.side = side;
    }

    @Override
    public double perimeter() {
        return 6 * side;
    }

    @Override
    public double area() {
        return (3 * Math.sqrt(3) * Math.pow(side, 2)) / 2;
    }
}
// se crean instancias de cada clase de figura geometrica, se guardan en un 
//array de tipo 'figure' gracias al polimorfismo, se hace un for each en cada figura
//se accede a cada figura y se lklaman a los metodos
public class Main {
    public static void main(String[] args) {
        Triangle triangle = new Triangle("Rojo", 3, 4, 5);
        Circle circle = new Circle("Azul", 5);
        Rectangle rectangle = new Rectangle("Verde", 4, 6);
        Hexagon hexagon = new Hexagon("Amarillo", 4);

        Figure[] figures = {triangle, circle, rectangle, hexagon};

        for (Figure figure : figures) {
            System.out.println("Color: " + figure.getColor());
            System.out.println("Perímetro: " + figure.perimeter());
            System.out.println("Área: " + figure.area());
            System.out.println();
        }
    }
}
