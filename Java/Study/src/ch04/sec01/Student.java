package ch04.sec01;

// 父类和接口有相同方法时，使用的是父类方法
public class Student extends Person implements Named {
    private int id;

    public Student(String name, int id) { super(name); this.id = id; }
    public int getId() { return id; }
}