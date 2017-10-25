package ch02.sec01;

import java.time.DayOfWeek;
import java.time.LocalDate;

public class Cal {
    public static void main(String[] args) {
        LocalDate date = LocalDate.now().withDayOfMonth(1); // 2017-10-01
        int month;
        if (args.length >= 2) {     // 终端是否传参， 参数格式：月 年
            month = Integer.parseInt(args[0]);
            int year = Integer.parseInt(args[1]);
            date = LocalDate.of(year, month, 1);
        } else {
            month = date.getMonthValue(); // 获得月份
        }
        
        System.out.println(" Mon Tue Wed Thu Fri Sat Sun");
        DayOfWeek weekday = date.getDayOfWeek(); // 今天周几
        int value = weekday.getValue(); // 1 = Monday, ... 7 = Sunday
        for (int i = 1; i < value; i++)
            System.out.print("    ");
        while (date.getMonthValue() == month) {
            System.out.printf("%4d", date.getDayOfMonth());
            date = date.plusDays(1);
            if (date.getDayOfWeek().getValue() == 1) // 如果是周一，那么在此之前我需要换行
                System.out.println();
        }
        if (date.getDayOfWeek().getValue() != 1)
           System.out.println();
    }
}
