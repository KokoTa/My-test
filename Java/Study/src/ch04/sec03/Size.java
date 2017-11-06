package ch04.sec03;

public enum Size {
    SMALL("S"), MEDIUM("M"), LARGE("L"), EXTRA_LARGE("XL");

    private String abbreviation; // 缩写

    Size(String abbreviation) { // 构造函数，枚举类型的构造函数只能是private，默认自动加private
        this.abbreviation = abbreviation;
    }

    public String getAbbreviation() { return abbreviation; }
}