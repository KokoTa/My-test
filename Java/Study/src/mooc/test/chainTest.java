package mooc.test;

// 课程1-3
public class chainTest {
    public static void main(String[] args) {
        chainTest ct = new chainTest();
        try {
            ct.test2();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public void test1() throws customException { // throws向上级抛出错误
        throw new customException("这是个自定义错误");
    }
    public void test2() {
        try {
            test1();
        } catch(customException e) {
            // 自定义事件需要RuntimeException调用
            RuntimeException newExc = new RuntimeException("这是个运行时错误");
            newExc.initCause(e);
            throw newExc;
        }
    }
}
