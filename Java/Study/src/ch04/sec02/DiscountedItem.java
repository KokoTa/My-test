package ch04.sec02;

import java.util.Objects;

public class DiscountedItem extends Item {
    private double discount;

    public DiscountedItem(String description, double price, double discount) {
        super(description, price);
        this.discount = discount;
    }

    public boolean equals(Object otherObject) {
        // 先比较父类，再比较子类
        if (!super.equals(otherObject)) return false;
        DiscountedItem other = (DiscountedItem) otherObject;
        return discount == other.discount;
    }
    
    public int hashCode() {
        return Objects.hash(super.hashCode(), discount);
    }
}