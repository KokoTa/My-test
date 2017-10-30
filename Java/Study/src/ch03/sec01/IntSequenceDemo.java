package ch03.sec01;

public class IntSequenceDemo {
    public static double average(IntSequence seq, int n) {
        int count = 0;
        double sum = 0;
        while (seq.hasNext() && count < n) {
            count++;
            sum += seq.next();
        }
        return count == 0 ? 0 : sum / count;
    }

    public static void main(String[] args) {
        SquareSequence squares = new SquareSequence();
        double avg = average(squares, 100);
        System.out.println("Average of first 100 squares: " + avg);

        IntSequence digits = new DigitSequence(1729);
        while (digits.hasNext()) System.out.print(digits.next() + " ");
        System.out.println();
        
        digits = new DigitSequence(1729);
        avg = average(digits, 100);
            // Will only look at the first four sequence values
        System.out.println("Average of the digits: " + avg);

        // 父类IntSequence转子类DIgitSequence
        IntSequence sequence = new DigitSequence(1000);
        DigitSequence other = (DigitSequence) sequence;
        System.out.println(other.rest());
        System.out.println(sequence instanceof DigitSequence);
        System.out.println(other instanceof DigitSequence);
    }
}
