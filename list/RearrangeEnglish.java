import java.util.Scanner;
import java.util.TreeSet;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
public class RearrangeEnglish{
    public static void main(String[] args) throws FileNotFoundException{
        File english = new File("english.txt");// original text file
        File cleanup = new File("cleanup.txt"); // cleaned up file with all words arranged in dictionary order

        Scanner sc=new Scanner(english);
        TreeSet <String> set=new TreeSet<String>();
        
        while(sc.hasNextLine())
            set.add(sc.nextLine());
        
        boolean flag=true;
        try {
            if (cleanup.createNewFile())
                {System.out.println("new file created " + cleanup.getName());
                flag=true;}
            else
                {System.out.println("File Already Present");
                    flag=false;}
                
        } catch (IOException e1) {
            // TODO Auto-generated catch block
            System.out.println("Problem creating fresh file "+e1);
            e1.printStackTrace();
        }

        try {
            FileWriter writer= new FileWriter("cleanup.txt",flag);

            for(String stopWord: set)
                writer.write(stopWord+"\n");
            
            writer.close();

        } catch (IOException e) {
            System.out.println("Cannot write to file "+e);
            e.printStackTrace();
        }
            
    }
}