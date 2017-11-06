package ch04.sec02;

import java.util.Objects;

public class Item {
    private String description;
    private double price;
        
    public Item(String description, double price) {
        this.description = description;
        this.price = price;
    }

    // 重写
    public boolean equals(Object otherObject) {
        // A quick test to see if the objects are identical
        // 引用是否相同
        if (this == otherObject) return true;
        // Must return false if the explicit parameter is null
        // 是否是null
        if (otherObject == null) return false;
        // Check that otherObject is a Item
        // 判断otherObject是否Item类型
        if (getClass() != otherObject.getClass()) return false;
        // Test whether the instance variables have identical values
        // 检查两者的实例变量是否相等
        Item other = (Item) otherObject;
        return Objects.equals(description, other.description)
            && price == other.price;
    }

    // 重写equals就也得重写hashCode
    public int hashCode() {
        return Objects.hash(description, price);
    }
}