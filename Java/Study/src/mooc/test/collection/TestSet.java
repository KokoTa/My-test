package mooc.test.collection;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TestSet {
    public List<Course> coursesToSelect;

    public TestSet() {
        coursesToSelect= new ArrayList<Course>();
    }

    public void testAdd() {
        Course cr1 = new Course("1", "课程1");
        coursesToSelect.add(cr1);
        Course cr2 = new Course("2", "课程2");
        coursesToSelect.add(cr2);
    }

    public void testForEach() {
        // 不用指定为Object然后再转Course，这是泛型的一个好处
        for(Course cr: coursesToSelect) {
            System.out.println(cr.id + " " + cr.name);
        }
    }

    // 打印输出课程(Set只能用forEach/iterator来获得元素，不能使用get()方法）
    public void testSetForEach(Student student) {
        for(Course cr: student.courses) {
            System.out.println(cr.id + " " + cr.name); // Set是无序存储，所以输出也是无序的。Set可以添加null这个空数据。
        }
    }

    public static void main(String[] args) {
        TestSet ts = new TestSet();
        ts.testAdd();
        ts.testForEach();
        // 创建学生对象
        Student student = new Student("1", "小明");
        System.out.println(student.name + "正在输入：");
        // 输入课程ID
        Scanner console = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            System.out.println("请输入课程ID");
            String courseId = console.next();
            for(Course cr: ts.coursesToSelect) {
                if(cr.id.equals(courseId)) {
                    student.courses.add(cr);
                }
            }
        }

        ts.testSetForEach(student);
    }
}
