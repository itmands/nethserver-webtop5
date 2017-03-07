import java.util.*;
import java.text.*;

public class ListLocales {
    static public void main(String[] args) {
        Locale list[] = DateFormat.getAvailableLocales();
        for (Locale aLocale : list) {
            System.out.println(aLocale.toString() + "\t" + aLocale.getDisplayName());
        }
    }
}

