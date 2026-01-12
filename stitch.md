<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>The Castle Hotel</title>
<!-- Fonts -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#1152d4",
                        "background-light": "#f6f6f8",
                        "background-dark": "#101622",
                    },
                    fontFamily: {
                        "display": ["Manrope", "sans-serif"]
                    },
                    borderRadius: {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                },
            },
        }
    </script>
</head>
<body class="bg-background-light dark:bg-background-dark font-display text-[#111318] dark:text-white antialiased">
<div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden">
<!-- Navigation -->
<header class="sticky top-0 z-50 flex items-center justify-between whitespace-nowrap border-b border-solid border-b-[#f0f2f4] bg-white/95 backdrop-blur px-10 py-3 dark:border-b-gray-800 dark:bg-[#101622]/95">
<div class="flex items-center gap-4 text-[#111318] dark:text-white">
<div class="size-8 text-primary">
<svg fill="currentColor" viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
<path d="M17 11V3H7v4H3v14h18V11h-4zm-8 4h2v2H9v-2zm2-4H9V9h2v2zm-2-4H7V5h2v2zm4 4h-2V9h2v2zm2 4h-2v-2h2v2zm-2-4h-2V5h2v6zM5 19v-6h2v6H5z"></path>
</svg>
</div>
<h2 class="text-lg font-bold leading-tight tracking-[-0.015em]">The Castle Hotel</h2>
</div>
<div class="flex flex-1 justify-end gap-8 items-center">
<nav class="hidden md:flex items-center gap-9">
<a class="text-sm font-medium leading-normal text-[#111318] hover:text-primary dark:text-gray-200 dark:hover:text-primary transition-colors" href="#">Home</a>
<a class="text-sm font-medium leading-normal text-[#111318] hover:text-primary dark:text-gray-200 dark:hover:text-primary transition-colors" href="#">Rooms</a>
<a class="text-sm font-medium leading-normal text-[#111318] hover:text-primary dark:text-gray-200 dark:hover:text-primary transition-colors" href="#">My Reservations</a>
<a class="text-sm font-medium leading-normal text-[#111318] hover:text-primary dark:text-gray-200 dark:hover:text-primary transition-colors" href="#">Contact Us</a>
</nav>
<div class="flex gap-4 items-center pl-4 border-l border-gray-200 dark:border-gray-700">
<div class="flex flex-col items-end hidden lg:flex">
<span class="text-xs text-gray-500 dark:text-gray-400">Signed in as</span>
<span class="text-sm font-semibold text-[#111318] dark:text-white truncate max-w-[180px]">alielhajj@outlook.de</span>
</div>
<button class="flex cursor-pointer items-center justify-center overflow-hidden rounded-lg h-9 px-4 bg-primary/10 text-primary hover:bg-primary hover:text-white transition-all text-sm font-bold leading-normal tracking-[0.015em]">
<span class="truncate">Log Out</span>
</button>
<div class="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-10 border-2 border-white dark:border-gray-800 shadow-sm" data-alt="User profile avatar showing a smiling person" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuDW4IZVYOVH7HNicmxtm2i0a4Fj7MUYTe3g6XrFiQ_AtvkEHTAdCXmNjs2d5jPo9WOlMLjDj-pTMEIOZ2nqsUIvwDuYCzy5wHi46WlXSxWTPSlQdsuTaMcskn0T9er4rhPMpHu3DBc3DxfXQphHnmnIds8OIxyeeObKZhKYUgsVOTJLPtjG7HzPPvrEDJriMKERZfiFk90-HLmTITSmZhhoLbFNmFGHdvyqiBfkRW62dazkf9V6QnATHo1X8lcGtQ0vIu2fiu0Wg6US");'>
</div>
</div>
</div>
</header>
<!-- Main Content -->
<main class="flex-1">
<!-- Hero Section -->
<section class="relative">
<div class="@container">
<div class="relative flex min-h-[600px] flex-col gap-6 bg-cover bg-center bg-no-repeat items-center justify-center p-8" data-alt="Luxurious hotel lobby with high ceilings and warm lighting" style='background-image: linear-gradient(rgba(0, 0, 0, 0.4) 0%, rgba(0, 0, 0, 0.6) 100%), url("https://lh3.googleusercontent.com/aida-public/AB6AXuD74tEslRX2NTKZegIYj7BMTX1yNtyI25JeEflSAsDZ1Fx9L4aCQ1eQH0YyhqHihK8EGEkXEGUWEO1UjWnlOJ_DTAnal5wEA3i2kv4OXrPQQn-8IwhJk9fzuvBiouJKeDgO2q9swn4FK4_M-odLrXXbnPpjY23ANDevZrLmj5cd_3J7ShTCVLAT7nMi3KIKChWz92nvrSBVPs_YSa4-4kViBzCWdumNgTBQ_6-nILoqkDRg7uPnc8rlzBhP_zTzDKWOkWUtAT25Gk1X");'>
<div class="flex flex-col gap-4 text-center max-w-[720px] animate-fade-in-up">
<h1 class="text-white text-5xl font-black leading-tight tracking-[-0.033em] drop-shadow-lg md:text-6xl">
                                Welcome to the Castle Hotel
                            </h1>
<h2 class="text-white/90 text-lg font-medium leading-relaxed md:text-xl drop-shadow-md">
                                Experience luxury and comfort in the heart of the city. Discover a sanctuary where modern elegance meets timeless tradition.
                            </h2>
</div>
<button class="flex mt-6 min-w-[160px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-8 bg-primary hover:bg-blue-700 transition-colors text-white text-base font-bold leading-normal tracking-[0.015em] shadow-lg hover:shadow-xl hover:-translate-y-0.5 transform duration-200">
<span class="truncate">View Rooms</span>
</button>
</div>
</div>
</section>
<!-- Services Section -->
<section class="py-16 px-4 md:px-10 lg:px-20 bg-background-light dark:bg-background-dark">
<div class="max-w-[1200px] mx-auto flex flex-col gap-12">
<!-- Headline -->
<div class="flex flex-col items-center gap-2">
<span class="text-primary font-bold tracking-wider uppercase text-sm">Amenities</span>
<h2 class="text-[#111318] dark:text-white tracking-tight text-3xl md:text-4xl font-bold leading-tight text-center">
                            Our Services
                        </h2>
<div class="h-1 w-20 bg-primary rounded-full mt-2"></div>
</div>
<!-- Grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6">
<!-- Card 1 -->
<div class="group flex flex-1 gap-4 rounded-xl border border-transparent bg-white dark:bg-[#1a2230] hover:border-primary/20 p-6 flex-col shadow-sm hover:shadow-md transition-all duration-300">
<div class="text-primary bg-primary/10 w-12 h-12 rounded-lg flex items-center justify-center group-hover:bg-primary group-hover:text-white transition-colors duration-300">
<span class="material-symbols-outlined text-[28px]">bed</span>
</div>
<div class="flex flex-col gap-2">
<h3 class="text-[#111318] dark:text-white text-lg font-bold leading-tight">Luxurious Rooms</h3>
<p class="text-gray-500 dark:text-gray-400 text-sm font-normal leading-normal">Elegant suites with city views and premium bedding.</p>
</div>
</div>
<!-- Card 2 -->
<div class="group flex flex-1 gap-4 rounded-xl border border-transparent bg-white dark:bg-[#1a2230] hover:border-primary/20 p-6 flex-col shadow-sm hover:shadow-md transition-all duration-300">
<div class="text-primary bg-primary/10 w-12 h-12 rounded-lg flex items-center justify-center group-hover:bg-primary group-hover:text-white transition-colors duration-300">
<span class="material-symbols-outlined text-[28px]">restaurant</span>
</div>
<div class="flex flex-col gap-2">
<h3 class="text-[#111318] dark:text-white text-lg font-bold leading-tight">Fine Dining</h3>
<p class="text-gray-500 dark:text-gray-400 text-sm font-normal leading-normal">Gourmet dishes from world-class chefs.</p>
</div>
</div>
<!-- Card 3 -->
<div class="group flex flex-1 gap-4 rounded-xl border border-transparent bg-white dark:bg-[#1a2230] hover:border-primary/20 p-6 flex-col shadow-sm hover:shadow-md transition-all duration-300">
<div class="text-primary bg-primary/10 w-12 h-12 rounded-lg flex items-center justify-center group-hover:bg-primary group-hover:text-white transition-colors duration-300">
<span class="material-symbols-outlined text-[28px]">spa</span>
</div>
<div class="flex flex-col gap-2">
<h3 class="text-[#111318] dark:text-white text-lg font-bold leading-tight">Spa &amp; Wellness</h3>
<p class="text-gray-500 dark:text-gray-400 text-sm font-normal leading-normal">Relaxing treatments, massages, and sauna.</p>
</div>
</div>
<!-- Card 4 -->
<div class="group flex flex-1 gap-4 rounded-xl border border-transparent bg-white dark:bg-[#1a2230] hover:border-primary/20 p-6 flex-col shadow-sm hover:shadow-md transition-all duration-300">
<div class="text-primary bg-primary/10 w-12 h-12 rounded-lg flex items-center justify-center group-hover:bg-primary group-hover:text-white transition-colors duration-300">
<span class="material-symbols-outlined text-[28px]">meeting_room</span>
</div>
<div class="flex flex-col gap-2">
<h3 class="text-[#111318] dark:text-white text-lg font-bold leading-tight">Conference Halls</h3>
<p class="text-gray-500 dark:text-gray-400 text-sm font-normal leading-normal">Modern spaces for business events and meetings.</p>
</div>
</div>
<!-- Card 5 -->
<div class="group flex flex-1 gap-4 rounded-xl border border-transparent bg-white dark:bg-[#1a2230] hover:border-primary/20 p-6 flex-col shadow-sm hover:shadow-md transition-all duration-300">
<div class="text-primary bg-primary/10 w-12 h-12 rounded-lg flex items-center justify-center group-hover:bg-primary group-hover:text-white transition-colors duration-300">
<span class="material-symbols-outlined text-[28px]">room_service</span>
</div>
<div class="flex flex-col gap-2">
<h3 class="text-[#111318] dark:text-white text-lg font-bold leading-tight">24/7 Room Service</h3>
<p class="text-gray-500 dark:text-gray-400 text-sm font-normal leading-normal">Round-the-clock service for your every need.</p>
</div>
</div>
</div>
</div>
</section>
<!-- Secondary Call to Action / Image Break -->
<section class="grid grid-cols-1 md:grid-cols-2 h-auto md:h-[500px]">
<div class="relative bg-cover bg-center h-[300px] md:h-full" data-alt="Interior view of a modern hotel suite bedroom" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuBkRR32udhHXH8eEj5kdoAn0FX8Ctf93H0dtZU2c9le2FOaWH9G4zpgtap9uzE519o93Eb0AgMv_MTCWK_CNzIaTLaKSK5fY75CQ1ZXMpteKozxT0TG4-hp5PN3Kv5XykpTzwPmBj2f6gI1m8H-nhOz7Y4ogQdN9eWOwmNFnTPmPNYiGDoT_Bs1U_hOXPhAnXpe1d3POSrZD0JNEEr9anzyratjadUPjooUiIWuS1G9hdj7H1gtC-WExgzGk_7_l032TeTJF_A4x1R4");'>
</div>
<div class="flex flex-col justify-center p-10 md:p-20 bg-white dark:bg-[#151c2b]">
<h3 class="text-3xl font-bold mb-4 text-[#111318] dark:text-white">A Stay to Remember</h3>
<p class="text-gray-600 dark:text-gray-300 text-lg mb-8 leading-relaxed">
                        Whether you are traveling for business or leisure, The Castle Hotel offers an unparalleled experience. Immerse yourself in our world of refined luxury.
                    </p>
<a class="text-primary font-bold text-lg hover:underline flex items-center gap-2" href="#">
                        Book Your Stay Now 
                        <span class="material-symbols-outlined text-sm">arrow_forward</span>
</a>
</div>
</section>
</main>
<!-- Footer -->
<footer class="bg-white dark:bg-[#101622] border-t border-gray-100 dark:border-gray-800">
<div class="flex flex-col gap-6 px-5 py-10 text-center items-center justify-center">
<div class="size-8 text-primary opacity-50">
<svg fill="currentColor" viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
<path d="M17 11V3H7v4H3v14h18V11h-4zm-8 4h2v2H9v-2zm2-4H9V9h2v2zm-2-4H7V5h2v2zm4 4h-2V9h2v2zm2 4h-2v-2h2v2zm-2-4h-2V5h2v6zM5 19v-6h2v6H5z"></path>
</svg>
</div>
<p class="text-gray-500 dark:text-gray-400 text-sm font-normal leading-normal">© 2025 The Castle Hotel, Inc. All rights reserved.</p>
<div class="flex gap-6 text-sm text-gray-400">
<a class="hover:text-primary transition-colors" href="#">Privacy Policy</a>
<a class="hover:text-primary transition-colors" href="#">Terms of Service</a>
</div>
</div>
</footer>
</div>
</body></html>