package ch04.sec05;

import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.Arrays;
import java.util.Scanner;

// 打印类的所有方法
public class MethodPrinter {
    public static void main(String[] args) throws ReflectiveOperationException {
        System.out.print("Class name: ");
        Scanner in = new Scanner(System.in);
        String className = in.nextLine();
        Class<?> cl = Class.forName(className); // 获得类
        while (cl != null) {
            for (Method m : cl.getDeclaredMethods()) { // 获得类的所有方法
                System.out.println(
                    Modifier.toString(m.getModifiers()) + " " + // 方法修饰符
                    m.getReturnType().getCanonicalName() + " " + // 方法返回类型
                    m.getName() + // 方法名
                    Arrays.toString(m.getParameters())); // 方法参数
            }
            cl = cl.getSuperclass(); // 上级类
        }
    }
}
