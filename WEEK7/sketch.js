var comicTable;

let number;

publishers = ["DC", "MARVEL", "IMAGE"];

var barWidth = 20;

var comicBook = []

function preload() {
  comicTable = loadTable("comics.csv","csv","header");
}

function setup() {
    createCanvas(1000, 530);
  angleMode(DEGREES);
  
  row = comicTable.getRowCount() 
  column = comicTable.getColumnCount()

  for (let r = 0; r < comicTable.getRowCount(); r++)
    for (let c = 0; c < comicTable.getColumnCount(); c++) {
    }


}

function draw() {
  background(153, 51, 0);
  noStroke();
  textSize(12);
  

  
    //the bars done manually, because I was unable to get cvs to work at all.
  
  //DC
    fill(153, 102, 51);
    noStroke();
    rect(80, 60, 25, 390); /*detective comics*/
    rect(110, 140, 25, 310);/*action comics*/
    rect(140, 200, 25, 250);/*dark knight*/
    rect(170, 230, 25, 220);  /*batman*/
    rect(200, 270, 25, 180);/*harley quinn*/
    rect(230, 280, 25, 170); /*jla*/
    rect(260, 300, 25, 150); /*rebirth*/
  
  //MARVEL
    fill(51, 153, 153);
    noStroke();
    rect(320, 35, 25, 415); /*star wars*/
    rect(350, 70, 25, 380); /*spiderman*/
    rect(380, 100, 25, 350);/*secret wars*/
    rect(410, 130, 25, 320);/*spiderman*/
    rect(440, 230, 25, 220);/*spiderman*/
    rect(470, 270, 25, 180);/*starwars*/
    rect(500, 300, 25, 150);/*civil war ii*/
  
  //IMAGE
  
    fill(223, 32, 32);
    noStroke();
    rect(560, 270, 25, 180);/*walking dead*/
    rect(590, 285, 25, 165);/*walking dead*/
    rect(620, 285, 25, 165);/*walking dead*/
    rect(650, 340, 25, 110);/*spawn*/
    rect(680, 370, 25, 80);/*spawn*/
    rect(710, 390, 25, 60);/*magic order*/
    rect(740, 390, 25, 60); /*walking dead*/
  
      
  if (mouseIsPressed) {

  
  //MARVEL

    fill(102, 255, 102);
    noStroke();
    textSize(12);
    
    rect(320, 35, 25, 415); /*star wars*/
    rect(350, 70, 25, 380); /*spiderman*/
    rect(380, 100, 25, 350);/*secret wars*/
    rect(410, 130, 25, 320);/*spiderman*/
    rect(440, 230, 25, 220);/*spiderman*/
    rect(470, 270, 25, 180);/*starwars*/
    rect(500, 300, 25, 150);/*civil war ii*/

    
   
}
  
  
  if (mouseIsPressed) {
    fill(153, 51, 255);
    noStroke();
    rect(80, 60, 25, 390); /*detective comics*/
    rect(110, 140, 25, 310);/*action comics*/
    rect(140, 200, 25, 250);/*dark knight*/
    rect(170, 230, 25, 220);  /*batman*/
    rect(200, 270, 25, 180);/*harley quinn*/
    rect(230, 280, 25, 170); /*jla*/
    rect(260, 300, 25, 150); /*rebirth*/
    
  }
  
      //graph lines
    fill(0);
    stroke('rgb(0,255,0)');
    line(70, 450, 770, 450);
    line(70, 450, 70, 10);
    
  
  {
  }
    

  {
  //x-points
    fill(0, 0, 0);
    stroke(0);
    textAlign(CENTER);
    textSize(20);    
    text('DC', 180,470);
    text('MARVEL', 430,470);
    text('IMAGE', 640,470);
  
  //y-numbers
    fill (0,0,0);
    stroke(0);
    textSize(16);
    text(0,50,449);
    text("100K",45,400);
    text("200K",45,350);
    text("300K",45,300);
    text("400K",45,250);
    text("450K",45,200);
    text("500K",45,150);
    text("550K",45,100);
    text("1M",45,50);
  
  // y-label
    textFont('Trebuchet MS');
    textSize(20);
    stroke(0)
    text('C',10, 160);
    text('O',10, 180);
    text('P',10, 200);
    text('I',10, 220);
    text('E',10, 240);
    text('S',10, 260);
    
    fill(255, 153, 51);
    stroke(255, 128, 0);
    rect(760, 80, 190, 270);
    
 
    rotate(35); 
    textSize(24); 
    text("GeeksForGeeks", 400, 50); 
  }
  //title
  fill(255);
  textFont('Trebuchet MS');
  textAlign(CENTER,CENTER);
  textSize(25);
  text("BEST SELLING COMIC BOOKS OF THE DECADE",405,510);
  

  
}