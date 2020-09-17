

//This is a stub for improving the code by using an array



//What would chanage below if the items array existed?

missValue = Math.trunc(Math.random() * 5) + 2;

function add() {


    startValue = Math.trunc(Math.random() * 10) + 1;

    item1.innerHTML = startValue;

 
    step = Math.trunc(Math.random() * 25) + 1;

    console.log(step)

    for (i = 2; i < 7; i++) 
    {
        startValue = startValue + step;

        val = (document.getElementById('item' + String(i)))

        if (i != missValue) 
        {
            val.innerHTML = startValue;
            console.log(startValue)
        }
        else
        {
            answer = startValue;
            val.addEventListener('click', function()
            {
                response = prompt("Enter the missing value");
                if (answer == response)
                {
                    alert("Congratulations - Correct");
                    (document.getElementById('item' + String(missValue))).innerHTML = response;

                    location.reload();

                }
                else
                    alert("Sorry, that is not correct.  Feel free to try again");     
                    location.reload();           
            });
        }
    }



}

function multiply(){

  startValue = Math.trunc(Math.random() * 10) + 1;

    item1.innerHTML = startValue;

 
    step = Math.trunc(Math.random() * 5) + 1;
    console.log(step)
    for (i = 2; i < 7; i++) 
    {
        startValue = startValue * step;

        val = (document.getElementById('item' + String(i)))

        if (i != missValue) 
        {
            val.innerHTML = startValue;
        }
        else
        {
            answer = startValue;
            val.addEventListener('click', function()
            {
                response = prompt("Enter the missing value");
                if (answer == response)
                {
                    alert("Congratulations - Correct");
                    (document.getElementById('item' + String(missValue))).innerHTML = response;

                    location.reload();
                }
                else
                    alert("Sorry, that is not correct.  Feel free to try again");     

                    location.reload();           
            });
        }
    }

}
