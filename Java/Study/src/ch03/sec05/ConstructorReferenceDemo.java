package ch03.sec05;

import java.util.ArrayList;

public class ConstructorReferenceDemo {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("Peter");
        names.add("Paul");
        names.add("Mary");
        Employee[] employees = names.stream().map(Employee::new).toArray(Employee[]::new); // map中的构造函数用于构造实例，toArray中的构造函数将Object类型转为Employee类型
        for (Employee e : employees) System.out.println(e.getName());
    }
}
