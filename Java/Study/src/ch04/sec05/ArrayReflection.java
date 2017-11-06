package ch04.sec05;

import java.lang.reflect.Array;
import java.util.Arrays;

// 扩展一个固定大小的数组
public class ArrayReflection {
    // 坏方法，构造一个新数组，把旧数组的值赋值过去
    // 并且这个坏方法会无效，因为返回的是Object，而不是传入的类型（比如Person类的数组）
    // 因为：Person -》 Object -》 Person 是可行的
    // Object-》 Person 不可行
    public static Object[] badCopyOf(Object[] array, int newLength) { // Not useful
        Object[] newArray = new Object[newLength];
        for (int i = 0; i < Math.min(array.length, newLength); i++)
            newArray[i] = array[i];
        return newArray;
    }

    // 好方法
    public static Object goodCopyOf(Object array, int newLength) {
        Class<?> cl = array.getClass(); // 首先获得类
        System.out.println(cl);

        if (!cl.isArray()) return null; // 类是否是数组
        Class<?> componentType = cl.getComponentType(); // 获得类中元素的类型为int
        System.out.println(componentType);

        int length = Array.getLength(array); // 获得原数组的长度
        System.out.println(length);

        Object newArray = Array.newInstance(componentType, newLength); // 利用newInstance构造新数组
        for (int i = 0; i < Math.min(length, newLength); i++) // 把旧数组数据迁移到新数组
            Array.set(newArray, i, Array.get(array,  i));
        return newArray;
    }
    
    public static void main(String[] args) {
        int[] primes = { 2, 3, 5, 7, 11 };
        primes = (int[]) goodCopyOf(primes, 10); // 返回的是一个Object，需要转换
        System.out.println(Arrays.toString(primes));
    }
}
