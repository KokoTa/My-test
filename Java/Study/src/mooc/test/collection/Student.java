package mooc.test.collection;

import java.util.HashSet;
import java.util.Set;

public class Student {
    public String id;
    public String name;

    public Set<Course> courses; // Set接口不能直接实例化

    public Student(String id, String name) {
        this.id = id;
        this.name = name;
        this.courses = new HashSet<>(); // 利用Set的支线类HashSet来初始化
    }
}
