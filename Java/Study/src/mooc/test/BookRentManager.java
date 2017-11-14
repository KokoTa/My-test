package mooc.test;

import java.util.Scanner;

// 课程1-4
public class BookRentManager {
    private static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        // 定义图书数组
        String[] books = {"数据结构", "算法", "JAVA核心技术"};
        // 指令判断
        while(true) {
            System.out.println("请输入命令：1-按名称查找；2-按序号查找");
            String book;
            // try catch 测试
            try {
                // 试图获得一个整数命令
                int command = inputCommand();
                // 根据不同命令值进行操作
                switch (command) {
                    case 1: // 书名选择
                        book = getBookByName(books);
                        System.out.println("找到图书:" + book);
                        break;
                    case 2: // 书序号
                        book = getBookByNumber(books);
                        System.out.println("找到图书:" + book);
                        break;
                    case -1: // 输入错误
                        System.out.println("输入出错");
                        break;
                    default: // 其他情况都判断为错误
                        System.out.println("输入错误");
                        break;
                }
                break; // 如果操作正确，则结束程序
            } catch (Exception e) {
                System.out.println(e.getMessage()); // 接收方法传出的错误信息并输出
            }
        }
    }

    // 获得整数值
    private static int inputCommand() {
        int command;
        // 判断是否是输入整数，不是则重置输入对象并抛出错误标记-1
        try {
            command = console.nextInt();
            return command;
        } catch (Exception e) {
            console = new Scanner(System.in);
            return -1;
        }
    }

    // 按名字找书
    public static String getBookByName(String[] books) throws Exception {
        System.out.println("请输入书名：");
        String name = console.next();
        // 查找
        for(int i = 0; i < books.length; i++) {
            if (name.equals(books[i])) {
                return books[i];
            }
        }
        // 没有匹配成功则抛出异常
        throw new Exception("图书不存在");
    }

    // 按序号找书
    public static String getBookByNumber(String[] books) throws Exception {
        System.out.println("请输入序号：");
        while (true) {
            try {
                // 试图获得一个整数
                int index = inputCommand();
                // 不是整数则抛出错误
                if(index == -1) {
                    System.out.println("请输入整数");
                    continue;
                }
                // 如果没有越界错误则返回书名
                String book = books[index];
                return book;
            } catch (ArrayIndexOutOfBoundsException e) { // 越界异常捕获
                Exception noExist = new Exception("图书不存在"); // 生成一个自定义错误对象
                noExist.initCause(e); // 将错误信息e传入错误对象
                throw noExist;
            }
        }
    }
}
