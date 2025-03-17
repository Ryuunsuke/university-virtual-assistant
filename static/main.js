$(document).ready(function(){
    $('#showRegister').click(function(e){
        e.preventDefault();
        $('.signin > .content').first().hide();  // Hide the login form
        $('#registerForm').show();               // Show the registration form
    });

    $('#registerFormSubmit').submit(function(e){
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/register',
            data: $(this).serialize(),
            success: function(response){
                alert(response.message);

                // Hide the registration form and show the login form
                $('#registerForm').hide();
                $('.signin > .content').first().show();
                $('#registerFormSubmit')[0].reset();  // Clear the registration form
            },
            error: function(){
                alert('Registration failed. Please try again.');
            }
        });
    });
});
