package mooc.test;

// 课程1-1
public class exception {
    public static void main(String[] args) {
        exception t = new exception();
        int result = t.test();
        System.out.println(result);
    }

    public int test() {
        int divider = 10;
        int result = 100;
        try {
            while(divider > -1) {
                divider--;
                result = result + 100/divider; // 100/0将报错
            }
        } catch(Exception e) {
            System.out.println("error");
            e.printStackTrace();
        } finally {
            System.out.println("finally");
        }
        System.out.println("end");
        return result = 100;
    }
}
