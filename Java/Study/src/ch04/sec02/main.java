package ch04.sec02;

public class main {
    public static void main(String[] args) {
        // toString方法测试
        Employee emp = new Employee("KokoTa", 5000);
        System.out.println(emp.toString());
        Manager mag = new Manager("KonoTa", 10000);
        System.out.println(mag.toString());
        // equals比较对象是看引用的，因此需要重写equals方法
        Employee n_emp = new Employee("KokoTa", 5000);
        System.out.println(emp.equals(n_emp));
    }
}
