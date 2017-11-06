package ch04.sec01;

public class StudentDemo {
    public static void main(String[] args) {
        Person p = new Student("Fred", 1729); // OK, a concrete subclass
        System.out.println(p.getName());
        Student s = (Student) p;
        System.out.println(s.getName());
        Named n = s; // 转为接口类时，接口类的默认方法被覆盖
        System.out.println(n.getName());
    }
}
