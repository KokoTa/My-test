package mooc.test.collection;

import java.util.ArrayList;
import java.util.List;

// 泛型，只能存放指定类型及其子类型的数据
// 泛型不能使用基本数据类型，应使用其包装类型，比如不能用int，要用Integer
public class TestGeneric {
    public List<Course> courses;

    public TestGeneric() {
        this.courses = new ArrayList<Course>();
    }

    // 添加指定类型数据
    public void testAdd() {
        Course cr1 = new Course("1", "课程1");
        courses.add(cr1);
        Course cr2 = new Course("2", "课程2");
        courses.add(cr2);
//        报错
//        courses.add("课程3");
    }

    // 输出
    public void testForEach() {
        // 不用指定为Object然后再转Course，这是泛型的一个好处
        for(Course cr: courses) {
            System.out.println(cr.id + " " + cr.name);
        }
    }

    // 添加子类型数据
    public void testChild() {
        ChildCourse ccr = new ChildCourse();
        ccr.id = "3";
        ccr.name = "子课程";
        courses.add(ccr);
    }

    public static void main(String[] args) {
        TestGeneric tg = new TestGeneric();
        tg.testAdd();
        tg.testChild();
        tg.testForEach();
    }
}
