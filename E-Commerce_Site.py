# E-Comm website
#The Front-End of the project is completed using HTML, CSS and Bootstrap.
#The Back-End is done using Python.
#installing xampp
#creating a new file name 'Website' in xampp folder to save the codes.

#Making SRS




#signup.html

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <title>Sign Up</title>
  </head>
  <body>
    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand">E-COMMERCE</a>
      <form class="form-inline">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Log In</button>
      </form>
    </nav>
    <div class="container">
      <form>
      <div class="form-group row">
        <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
        </div>
      </div>
      <div class="form-group row">
        <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
        </div>
      </div>
      <div class="form-group row">
        <label for="inputUsername" class="col-sm-2 col-form-label">Username</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="inputUsername" placeholder="Username">
        </div>
      </div>
      
      <div class="form-group row">
        <div class="col-sm-10">
          <button type="submit" class="btn btn-primary">Sign Up</button>
          <br>
          <a href="login.html">Already a user? Login here.</a>
        </div>
      </div>
    </form>
    </div>
    

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>






#Login.html

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <title>Log In</title>
  </head>
  <body>
    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand">E-COMMERCE</a>
      <form class="form-inline">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Sign Up</button>
      </form>
    </nav>
    <div class="container">
      <form>
      <div class="form-group row">
        <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
        </div>
      </div>
      <div class="form-group row">
        <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
        </div>
      </div>
      
      <div class="form-group row">
        <div class="col-sm-10">
          <button type="submit" class="btn btn-primary">Log In</button>
          <br>
          <a href="signup.html">Don't have an account? Sign up here.</a>
        </div>
      </div>
    </form>
    </div>
    

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>






#product
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <title>Products</title>
  </head>
  <body>
    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand">E-COMMERCE</a>
      <form class="form-inline">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Login</button>
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Sign Up</button>
      </form>
    </nav>
    <div class="container">
      <div class="card-group">
        <div class="card">
          <img class="card-img-top" src="https://images.unsplash.com/photo-1516962126636-27ad087061cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">Polaroid Camera</h5>
            <h6>Category : Camera</h6>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <p class="card-text"><button class="btn btn-primary">View Details</button></p>
          </div>
        </div>
        <div class="card">
          <img class="card-img-top" src="https://images.unsplash.com/photo-1622760807800-66cf1466fc08?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1965&q=80" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">Sneakers</h5>
            <h6>Category : Shoes</h6>
            <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p>
            <p class="card-text"><button class="btn btn-primary">View Details</button></p>
          </div>
        </div>
        <div class="card">
          <img class="card-img-top" src="https://images.unsplash.com/photo-1603816245457-fe9c80b740ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=433&q=80" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">Apple iPhone</h5>
            <h6>Category : Phone</h6>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
            <p class="card-text"><button class="btn btn-primary">View Details</button></p>
          </div>
        </div>
      </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>







#View Details

<!DOCTYPE html>
<html lang="en">
  <head>
    
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Product Detail</title>
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <style type="text/css">
    
    /*****************globals*************/
    body {
      font-family: 'open sans';
      overflow-x: hidden; }

    img {
      max-width: 100%; }

    .preview {
      display: -webkit-box;
      display: -webkit-flex;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-orient: vertical;
      -webkit-box-direction: normal;
      -webkit-flex-direction: column;
          -ms-flex-direction: column;
              flex-direction: column; }
      @media screen and (max-width: 996px) {
        .preview {
          margin-bottom: 20px; } }

    .preview-pic {
      -webkit-box-flex: 1;
      -webkit-flex-grow: 1;
          -ms-flex-positive: 1;
              flex-grow: 1; }

    .preview-thumbnail.nav-tabs {
      border: none;
      margin-top: 15px; }
      .preview-thumbnail.nav-tabs li {
        width: 18%;
        margin-right: 2.5%; }
        .preview-thumbnail.nav-tabs li img {
          max-width: 100%;
          display: block; }
        .preview-thumbnail.nav-tabs li a {
          padding: 0;
          margin: 0; }
        .preview-thumbnail.nav-tabs li:last-of-type {
          margin-right: 0; }

    .tab-content {
      overflow: hidden; }
      .tab-content img {
        width: 100%;
        -webkit-animation-name: opacity;
                animation-name: opacity;
        -webkit-animation-duration: .3s;
                animation-duration: .3s; }

    .card {
      margin-top: 50px;
      background: #eee;
      padding: 3em;
      line-height: 1.5em; }

    @media screen and (min-width: 997px) {
      .wrapper {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex; } }

    .details {
      display: -webkit-box;
      display: -webkit-flex;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-orient: vertical;
      -webkit-box-direction: normal;
      -webkit-flex-direction: column;
          -ms-flex-direction: column;
              flex-direction: column; }

    .colors {
      -webkit-box-flex: 1;
      -webkit-flex-grow: 1;
          -ms-flex-positive: 1;
              flex-grow: 1; }

    .product-title, .price, .sizes, .colors {
      text-transform: UPPERCASE;
      font-weight: bold; }

    .checked, .price span {
      color: #ff9f1a; }

    .product-title, .rating, .product-description, .price, .vote, .sizes {
      margin-bottom: 15px; }

    .product-title {
      margin-top: 0; }

    .size {
      margin-right: 10px; }
      .size:first-of-type {
        margin-left: 40px; }

    .color {
      display: inline-block;
      vertical-align: middle;
      margin-right: 10px;
      height: 2em;
      width: 2em;
      border-radius: 2px; }
      .color:first-of-type {
        margin-left: 20px; }

    .add-to-cart, .like {
      background: #ff9f1a;
      padding: 1.2em 1.5em;
      border: none;
      text-transform: UPPERCASE;
      font-weight: bold;
      color: #fff;
      -webkit-transition: background .3s ease;
              transition: background .3s ease; }
      .add-to-cart:hover, .like:hover {
        background: #b36800;
        color: #fff; }

    .not-available {
      text-align: center;
      line-height: 2em; }
      .not-available:before {
        font-family: fontawesome;
        content: "\f00d";
        color: #fff; }

    .orange {
      background: #ff9f1a; }

    .green {
      background: #85ad00; }

    .blue {
      background: #0076ad; }

    .tooltip-inner {
      padding: 1.3em; }

    @-webkit-keyframes opacity {
      0% {
        opacity: 0;
        -webkit-transform: scale(3);
                transform: scale(3); }
      100% {
        opacity: 1;
        -webkit-transform: scale(1);
                transform: scale(1); } }

    @keyframes opacity {
      0% {
        opacity: 0;
        -webkit-transform: scale(3);
                transform: scale(3); }
      100% {
        opacity: 1;
        -webkit-transform: scale(1);
                transform: scale(1); } }

    /*# sourceMappingURL=style.css.map */
    </style>

  </head>

  <body>
      <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand">E-COMMERCE</a>
      <form class="form-inline">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Login</button>
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Sign Up</button>
      </form>
    </nav>
	
	<div class="container">
		<div class="card">
			<div class="container-fliud">
				<div class="wrapper row">
					<div class="preview col-md-6">
						
						<div class="preview-pic tab-content">
						  <div class="tab-pane active" id="pic-1"><img src="http://placekitten.com/400/252" /></div>
						  <div class="tab-pane" id="pic-2"><img src="http://placekitten.com/400/252" /></div>
						  <div class="tab-pane" id="pic-3"><img src="http://placekitten.com/400/252" /></div>
						  <div class="tab-pane" id="pic-4"><img src="http://placekitten.com/400/252" /></div>
						  <div class="tab-pane" id="pic-5"><img src="http://placekitten.com/400/252" /></div>
						</div>
						<ul class="preview-thumbnail nav nav-tabs">
						  <li class="active"><a data-target="#pic-1" data-toggle="tab"><img src="http://placekitten.com/200/126" /></a></li>
						  <li><a data-target="#pic-2" data-toggle="tab"><img src="http://placekitten.com/200/126" /></a></li>
						  <li><a data-target="#pic-3" data-toggle="tab"><img src="http://placekitten.com/200/126" /></a></li>
						  <li><a data-target="#pic-4" data-toggle="tab"><img src="http://placekitten.com/200/126" /></a></li>
						  <li><a data-target="#pic-5" data-toggle="tab"><img src="http://placekitten.com/200/126" /></a></li>
						</ul>
						
					</div>
					<div class="details col-md-6">
						<h3 class="product-title">men's shoes fashion</h3>
						<div class="rating">
							<div class="stars">
								<span class="fa fa-star checked"></span>
								<span class="fa fa-star checked"></span>
								<span class="fa fa-star checked"></span>
								<span class="fa fa-star"></span>
								<span class="fa fa-star"></span>
							</div>
							<span class="review-no">41 reviews</span>
						</div>
						<p class="product-description">Suspendisse quos? Tempus cras iure temporibus? Eu laudantium cubilia sem sem! Repudiandae et! Massa senectus enim minim sociosqu delectus posuere.</p>
						<h4 class="price">current price: <span>$180</span></h4>
						<p class="vote"><strong>91%</strong> of buyers enjoyed this product! <strong>(87 votes)</strong></p>
						<h5 class="sizes">sizes:
							<span class="size" data-toggle="tooltip" title="small">s</span>
							<span class="size" data-toggle="tooltip" title="medium">m</span>
							<span class="size" data-toggle="tooltip" title="large">l</span>
							<span class="size" data-toggle="tooltip" title="xtra large">xl</span>
						</h5>
						<h5 class="colors">colors:
							<span class="color orange not-available" data-toggle="tooltip" title="Not In store"></span>
							<span class="color green"></span>
							<span class="color blue"></span>
						</h5>
						<div class="action">
							<button class="add-to-cart btn btn-default" type="button">add to cart</button>
							<button class="like btn btn-default" type="button"><span class="fa fa-heart"></span></button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
  </body>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
</html>





   
