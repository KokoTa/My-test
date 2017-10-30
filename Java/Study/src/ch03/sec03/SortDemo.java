package ch03.sec03;

import java.util.Arrays;
import java.util.Comparator;

public class SortDemo {
    public static void main(String[] args) {
        String[] friends = { "Peter", "Paul", "Mary" };
        Arrays.sort(friends); // friends is now ["Mary", "Paul", "Peter"]
        System.out.println(Arrays.toString(friends));
        
        friends = new String[] { "PAC", "P", "PA" };
        Arrays.sort(friends, new LengthComparator()); // 第二个参数是比较类的实例
        System.out.println(Arrays.toString(friends));
    }
}

class LengthComparator implements Comparator<String> { // 调用Cmparator接口来自定义比较类
    public int compare(String first, String second) {
        return first.length() - second.length();
    }
}
