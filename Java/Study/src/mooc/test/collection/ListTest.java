package mooc.test.collection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

/**
 * 备选课程
 */
public class ListTest {
    public List coursesToSelect; // List类等顶层类不能实例化

    public ListTest() {
        this.coursesToSelect = new ArrayList(); // 用支线类进行实例化
    }

    public void testAdd() {
        // 尾部添加单元素
        Course cr1 = new Course("1", "数据结构");
        coursesToSelect.add(cr1);

        // 指定位置添加单元素
        Course cr2 = new Course("2", "JAVA");
        coursesToSelect.add(1, cr2);

        // 尾部添加集合
        Course[] crs = {new Course("3", "PHP"), new Course("4", "mySql")};
        coursesToSelect.addAll(Arrays.asList(crs));

        // 指定位置添加集合
        Course[] crs2 = {new Course("5", "Js"), new Course("6", "Spring")};
        coursesToSelect.addAll(0, Arrays.asList(crs2));

    }

    // 循环
    public void testGet() {
        int size = coursesToSelect.size();
        System.out.println("Get course1:");
        for(int i=0; i<size; i++) {
            // 对象存入集合会变为Object，取出时需要类型转换
            Course cr = (Course) coursesToSelect.get(i);
            System.out.println(cr.id + " " + cr.name);
        }
    }

    // 迭代
    public void testIterator() {
        Iterator it = coursesToSelect.iterator();
        System.out.println("Get Course2:");
        while(it.hasNext()) {
            Course cr = (Course) it.next();
            System.out.println(cr.id + " " + cr.name);
        }
    }

    // for each
    public void testForEach() {
        System.out.println("Get Course3:");
        for(Object obj: coursesToSelect) {
            Course cr = (Course) obj;
            System.out.println(cr.id + " " + cr.name);
        }
    }

    // 修改
    public void testModify() {
        coursesToSelect.set(4, new Course("7", "Other"));
    }

    // 删除
    public void testRemove() {
        coursesToSelect.remove(4);

        Course[] crs = {(Course) coursesToSelect.get(0), (Course) coursesToSelect.get(1)};
        coursesToSelect.removeAll(Arrays.asList(crs));
    }

    public static void main(String[] args) {
        ListTest lt = new ListTest();
        lt.testAdd();
        lt.testModify();
        lt.testRemove();
        lt.testGet();
        lt.testIterator();
        lt.testForEach();
    }
}


