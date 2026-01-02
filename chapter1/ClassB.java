package chapter1;

import packagea.ClassA;
public class ClassB extends ClassA{

    public void display() {
        System.out.println("Class b display method");
    }

    public static void main(String[] args) {
        System.out.println("B class");

        ClassA obj1 = new ClassA();
        obj1.display();

        ClassB obj2 = new ClassB();
        obj2.show2();
    }
}
