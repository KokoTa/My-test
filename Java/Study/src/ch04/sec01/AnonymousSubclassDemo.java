package ch04.sec01;

import java.util.ArrayList;

public class AnonymousSubclassDemo {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<String>(100) { // {...}是匿名子类，更改ArrayList的add函数
            public void add(int index, String element) {
                super.add(index, element);
                System.out.printf("Adding %s at %d\n", element, index);
            }
        };
        
        names.add(0, "Peter");
        names.add(1, "Paul");
        names.add(0, "Mary");
        System.out.println(names);
        
        invite(new ArrayList<String>() {{ add("Harry"); add("Sally"); }}); // 匿名子类进行数据初始化
    }
    
    public static void invite(ArrayList<String> friends) {
        System.out.println("Guest list: " + friends);
    }
}
