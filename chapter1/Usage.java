package chapter1;

import shape.Rectangle;

public class Usage {

    public static void main(String[] args) {
        Rectangle obj = new Rectangle();

        int area = obj.getArea();

        System.out.println("Area" + area);
    }

}
