public class test {
    public static void method() {
        System.out.println("Greeting");
    }
    public static void useMethod() {
        method();
    }
    public static void main(String[] args) {
        test2 x = new test2();
        test2.method();
    }
}
