#title = input("Enter your website title here: ")
ph = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <!--Important meta tags-->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <!--Website Title-->
    <title>Aditya Livestocks Farming</title>
    <!--Favicon-->
    <link rel="shortcut icon" href="images/favicon/favicon.png">
    <!--Google fonts-->
    <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Teko:wght@300;400;500;600;700&display=swap'>
    <link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;600;700&display=swap" rel="stylesheet">
    <!--jQuery Custom-->
    <script src='js/jquery-3.6.0.min.js'></script>
    <!--Fontawesome Icons-->
    <link rel='stylesheet' href='css/fontawesome_css/all.min.css'>
    <script src='js/fontawesome_js/all.min.js'></script>
    <!--Owl-Carousel-->
    <link rel="stylesheet" href="css/owl-carousel/owl.carousel.min.css">
    <link rel="stylesheet" href="css/owl-carousel/owl.theme.default.min.css">
    <script src='js/owl-carousel/owl.carousel.min.js'></script>
    <!--Responsive tabs-->
    <link rel="stylesheet" href='css/responsive-tabs/responsive-tabs.css'>
    <script src='js/responsive-tabs/jquery.responsiveTabs.min.js'></script>
    <!--Magnific Popup-->
    <link rel="stylesheet" href="css/magnific-popup/magnific-popup.css">
    <script src='js/magnific-popup/jquery.magnific-popup.min.js'></script>
    <!--Waypoints-->
    <script src='js/waypoints/jquery.waypoints.min.js'></script>
    <!--Counter-->
    <script src='js/counter/jquery.counterup.min.js'></script>
    <!--Isotope-->
    <script src='js/isotope/isotope.pkgd.min.js'></script>
    <!--Custom Bootstrap-->
    <link rel='stylesheet' href='css/bootstrap_css/bootstrap.css'>
    <script src='js/bootstrap_js/bootstrap.js'></script>

    <!--Custom JS-->
    <script src='js/myscript.js'></script>
    <!--CSS Custom-->
    <link rel="stylesheet" href="css/mystyle.css">
</head>

<body data-spy="scroll" data-target=".navbar" data-offset="75">
"""
nav = f"""
<!--Preloader-->
    <div id="preloader">
        <div id="preloader_status"></div>
    </div>
    <!--Preloader Ends-->
    <!--header-->
    <header>
        <nav class="navbar navbar-expand-md fixed-top white-nav-top">
            <!--Logo-->
            <a class="navbar-brand smooth-scroll" href="web.html">
                <img src='images/logos/favicon.png' alt='Logo'>
            </a>
            <!--
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  -->
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link  smooth-scroll" href="web.html">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link  smooth-scroll" href="about.html">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link  smooth-scroll" href="services.html">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link  smooth-scroll" href="contact.html">Contact</a>
                    </li>

                </ul>
            </div>
        </nav>
    </header>
    <!--Header Ends-->
"""
content = f"""
<!--Home-->
    <section id="home">
        <!--Background video-->
        <video id='home-bg-video' poster="images/home-poster/poster.jpg" autoplay muted loop>
            <source src='videos/home-video.mp4' type='video/mp4'>
            <source src='videos/home-video.ogv' type='video/ogv'>
            <source src='videos/home-video.webm' type='video/webm'>
        </video>
        <!--Overlay-->
        <div id="home-overlay">

        </div>
        <!--Home Content-->
        <div id="home-content">
            <div id="home-content-inner" class='text-center'>
                <div id="home-heading">
                    <h1 id="home-heading-1">Aditya</h1>
                    <h1 id="home-heading-2"><span>Livestocks</span> Farming</h1>
                </div>
                <div id="home-text">
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.Lorem ipsum dolor sit amet, consectetur adipisicing elit.Lorem ipsum.</p>
                </div>
                <div id="home-btn">
                    <a class='btn btn-general btn-home smooth-scroll' role='button' title='start now' href='#about'>Start Now</a>
                </div>
            </div>
        </div>
        <!--Arrow Down-->
        <a href='#about' id='arrow-down' class='smooth-scroll'>
            <i class='fas fa-angle-down'></i>
        </a>
    </section>
    <!--Home Ends-->
    <!--About-->
    <section id="about">
        <!--About 01-->
        <div id="about-01">
            <div class="content-box-lg">
                <div class="container">
                    <div class="row">
                        <!--About Left-->
                        <div class="col-md-6">
                            <div id="about-left">
                                <div class="vertical-heading">
                                    <h5>Who we are</h5>
                                    <h2><strong>A Story</strong><br> About Us</h2>
                                </div>
                            </div>
                        </div>
                        <!--About Right-->
                        <div class="col-md-6">
                            <div id="about-right">
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. In quisquam, quaerat aspernatur repellat veniam repudiandae, assumenda a! Error veritatis, accusantium assumenda? Reprehenderit repellendus repudiandae odit voluptates laudantium similique placeat, est.</p>
                            </div>
                        </div>
                    </div>
                    <!--About Bottom-->
                    <div class="row">
                        <div class="col-md-12">
                            <div id="about-bottom">
                                <img src='images/about/about-us.jpg' class='img-fluid' alt='About Us'>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--About 01 ends-->
        <!--About 02-->
        <div id="about-02">
            <div class="content-box-md">
                <div class="container">
                    <div class="row">
                        <div class="col-md-4">
                            <div class="about-item text-center">
                                <span><i class="fas fa-rocket"></i></span>
                                <h3>Mission</h3>
                                <hr>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui ratione, voluptatibus odit est eos itaque doloremque eligendi praesentium mollitia minima non quia, accusantium dolore. Nihil incidunt perferendis atque recusandae quaerat.</p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="about-item text-center">
                                <span><i class="fas fa-eye"></i></span>
                                <h3>Vision</h3>
                                <hr>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui ratione, voluptatibus odit est eos itaque doloremque eligendi praesentium mollitia minima non quia, accusantium dolore. Nihil incidunt perferendis atque recusandae quaerat.</p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="about-item text-center">
                                <span><i class='fas fa-dot-circle'></i></span>
                                <h3>Passion</h3>
                                <hr>
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui ratione, voluptatibus odit est eos itaque doloremque eligendi praesentium mollitia minima non quia, accusantium dolore. Nihil incidunt perferendis atque recusandae quaerat.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--About 02 ends-->
    </section>
    <!--About ends-->
    <!-- Map -->
    <section id="map">
       <div class="content-box-md">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3807.115543714464!2d78.46687141413227!3d17.406241806844275!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb975dd124c005%3A0x59439ffad6e0298e!2sBirla%20Mandir!5e0!3m2!1sen!2sin!4v1600749948324!5m2!1sen!2sin" width="100%" height="600" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
                </div>
            </div>
        </div>
        </div>
    </section>
    <!--Map Ends-->
"""
pb = """
<!-- Footer -->
    <footer class='text-center'>
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <p>Copyright &copy; 2020 All Rights Reserved by <span>Aditya Livestocks Ltd.</span></p>
                </div>
            </div>
        </div>
        <a id='back-to-top' class='btn btn-sm btn-general btn-yellow smooth-scroll' role='button' title='Submit' href='web.html'><i class="fas fa-angle-up"></i></a>
    </footer>
    <!--Footer Ends-->

</body>

</html>
"""
file = open("about.html", "w")
file.write(ph + nav + content + pb)
file.close()
print("Successfully created website!")