package mooc.test;

// 课程1-2
public class customException extends Exception {
    public static void main(String[] args) {

    }

    public customException(){

    }

    public customException(String message) {
        super(message); // 数据传给父类
    }
}
