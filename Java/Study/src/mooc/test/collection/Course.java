package mooc.test.collection;

public class Course {
    public String id;
    public String name;

    public Course(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public Course() {} // ChildCourse继承需要用到Course的无参构造函数
}
