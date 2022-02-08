import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.io.IOException;
import java.util.Scanner; // Import the Scanner class to read text files
import java.io.FileWriter;   // Import the FileWriter class

import java.io.BufferedWriter;
public class index {
    public static void main(String[] args) {
        int count = 0;
        //create file
        try {
            File myObj = new File("final_log.txt");
            if (myObj.createNewFile()) {
                System.out.println("File created: " + myObj.getName());
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }


        //Pattern pattern = Pattern.compile("\d+", Pattern.CASE_INSENSITIVE);
        try {
            File myObj = new File("log.txt");
            Scanner myReader = new Scanner(myObj);
            boolean status =true;
            String filename="";
            String rowscopied="";
            String total="";
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();

                if (!data.equals("")) {
                    //Matcher matcher = pattern.matcher(data);
                    String[] arrOfStr = data.split(" ", 8);

                    if (count % 3 == 0 && count != 0) {
                        System.out.println(filename+", "+rowscopied+", "+total);
                        try {
                            //FileWriter myWriter = new FileWriter("final_log.txt");
                            //myWriter.write(filename+", "+rowscopied+", "+total);
                            //myWriter.close();

                            File file = new File("final_log.txt");
                            FileWriter fr = new FileWriter(file, true);
                            BufferedWriter br = new BufferedWriter(fr);
                            br.write(filename+", "+rowscopied+", "+total+"\n");

                            br.close();
                            fr.close();

                        } catch (IOException e) {
                            System.out.println("An error occurred.");
                            e.printStackTrace();
                        }
                    }

                    if (arrOfStr[0].equals("----------") && status) {
//                        System.out.print(arrOfStr[1]+", ");
                        filename = arrOfStr[1];
                        status =false;
                        count++;
                    }
                    else if (arrOfStr[1].equals("rows")) {
//                        System.out.print(arrOfStr[0]+", ");
                        rowscopied = arrOfStr[0];
                        count++;
                    }
                    else if (arrOfStr[0].equals("Clock")) {
//                        System.out.println(arrOfStr[5]);
                        total = arrOfStr[5];
                        status =true;
                        count++;
                    }


//                    System.out.println(arrOfStr[1]);
                    //System.out.println(data);
                }

            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }
}
