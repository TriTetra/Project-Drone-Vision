# OpenCV Experiments & Learning Hub

Welcome to the OpenCV learning hub! This document provides a structured guide to the concepts, techniques, and applications covered in this project's `experiments` directory. Each section explains a core idea and links directly to the relevant Python scripts for hands-on learning.

---

## 1. Core Concepts: The Building Blocks

Before diving into complex techniques, it's crucial to understand the fundamentals of how OpenCV handles images.

### 1.1. The Image as a NumPy Array
In OpenCV, an image is fundamentally a multi-dimensional NumPy array. This allows for powerful and efficient pixel manipulation.
- **Key Idea:** A color image is a 3D array (`height x width x channels`), where "channels" typically represent Blue, Green, and Red (BGR). A grayscale image is a 2D array.
- **Relevant Script:**
  - [`./experiments/2_drawing_and_interaction/examples/01_image_as_numpy.py`](./experiments/2_drawing_and_interaction/examples/01_image_as_numpy.py)

### 1.2. Reading, Writing, and Resizing
The most basic operations involve loading images from files, displaying them, saving them, and changing their dimensions.
- **Key Idea:** Learn to handle different image file types and resize images while maintaining (or intentionally changing) the aspect ratio.
- **Relevant Scripts:**
  - [`./experiments/1_image_basics/examples/01_image_properties.py`](./experiments/1_image_basics/examples/01_image_properties.py)
  - [`./experiments/1_image_basics/examples/02_load_and_resize.py`](./experiments/1_image_basics/examples/02_load_and_resize.py)
  - [`./experiments/1_image_basics/examples/03_resize_aspect_ratio.py`](./experiments/1_image_basics/examples/03_resize_aspect_ratio.py)

### 1.3. Pixel Manipulation & Region of Interest (ROI)
You can access and modify individual pixel values or work with specific rectangular sections of an image.
- **Key Idea:** An ROI is a powerful concept for isolating a part of an image to apply a specific operation or analysis.
- **Relevant Scripts:**
  - [`./experiments/1_image_basics/examples/04_pixel_manipulation.py`](./experiments/1_image_basics/examples/04_pixel_manipulation.py)
  - [`./experiments/1_image_basics/examples/05_region_of_interest.py`](./experiments/1_image_basics/examples/05_region_of_interest.py)

---

## 2. Drawing and Interaction

This section covers how to draw shapes and text on images and how to build interactive applications that respond to user input.

- **Key Idea:** Add visual information to images or create simple graphical user interfaces for your vision applications.
- **Relevant Scripts:**
  - **Drawing:**
    - [`./experiments/2_drawing_and_interaction/examples/02_drawing_primitives.py`](./experiments/2_drawing_and_interaction/examples/02_drawing_primitives.py)
    - [`./experiments/2_drawing_and_interaction/examples/03_writing_text.py`](./experiments/2_drawing_and_interaction/examples/03_writing_text.py)
    - [`./experiments/6_applications_and_exercises/examples/02_mouse_drawing.py`](./experiments/6_applications_and_exercises/examples/02_mouse_drawing.py)
  - **Interaction:**
    - [`./experiments/2_drawing_and_interaction/examples/04_interactive_trackbar.py`](./experiments/2_drawing_and_interaction/examples/04_interactive_trackbar.py)
    - [`./experiments/6_applications_and_exercises/examples/01_hsv_calibration_tool.py`](./experiments/6_applications_and_exercises/examples/01_hsv_calibration_tool.py)

---

## 3. Video and Webcam

Learn how to process real-time video streams from files or a live webcam.
- **Key Idea:** A video is essentially a sequence of images (frames). The same techniques used on static images can be applied to each frame of a video.
- **Relevant Scripts:**
  - [`./experiments/3_video_and_webcam/examples/01_read_from_video_file.py`](./experiments/3_video_and_webcam/examples/01_read_from_video_file.py)
  - [`./experiments/3_video_and_webcam/examples/02_capture_from_webcam.py`](./experiments/3_video_and_webcam/examples/02_capture_from_webcam.py)

---

## 4. Image Processing Techniques

This is the core of computer vision, where you transform images to enhance features, reduce noise, or extract information.

### 4.1. Color Spaces
- **Key Idea:** The default BGR color space is not always ideal. The HSV (Hue, Saturation, Value) space is often better for color-based object detection because it separates color information (Hue) from intensity.
- **Relevant Script:**
  - [`./experiments/4_image_processing/examples/03_color_spaces.py`](./experiments/4_image_processing/examples/03_color_spaces.py)

### 4.2. Image Arithmetic and Blending
- **Key Idea:** Combine images together, for example, to create a "watermark" effect.
- **Relevant Scripts:**
  - [`./experiments/4_image_processing/examples/01_image_addition.py`](./experiments/4_image_processing/examples/01_image_addition.py)
  - [`./experiments/4_image_processing/examples/02_weighted_addition.py`](./experiments/4_image_processing/examples/02_weighted_addition.py)

### 4.3. Smoothing and Blurring
- **Key Idea:** Reduce image noise (e.g., from camera sensors) using various filters like Gaussian Blur and Median Blur. This is often a crucial preprocessing step.
- **Relevant Script:**
  - [`./experiments/4_image_processing/examples/04_image_smoothing.py`](./experiments/4_image_processing/examples/04_image_smoothing.py)

### 4.4. Thresholding & Morphological Operations
- **Key Idea:**
  - **Thresholding:** Simplify an image into a binary (black and white) form, which is essential for feature extraction.
  - **Morphology:** Clean up binary images using operations like Erosion (to remove noise) and Dilation (to close gaps).
- **Relevant Scripts:**
  - [`./experiments/4_image_processing/examples/06_thresholding.py`](./experiments/4_image_processing/examples/06_thresholding.py)
  - [`./experiments/4_image_processing/examples/07_morphological_ops.py`](./experiments/4_image_processing/examples/07_morphological_ops.py)

### 4.5. Bitwise Operations
- **Key Idea:** Use logical operations (AND, OR, NOT, XOR) to create masks and isolate specific regions of an image, such as an object identified by color.
- **Relevant Script:**
  - [`./experiments/4_image_processing/examples/05_bitwise_operations.py`](./experiments/4_image_processing/examples/05_bitwise_operations.py)

---

## 5. Feature Detection and Analysis

This section focuses on identifying interesting points, shapes, and objects within an image.

### 5.1. Edge and Corner Detection
- **Key Idea:** Find important structural features in an image. Edges represent boundaries, and corners are key points for tracking and matching.
- **Relevant Scripts:**
  - [`./experiments/5_feature_detection/examples/04_canny_edge_detection.py`](./experiments/5_feature_detection/examples/04_canny_edge_detection.py)
  - [`./experiments/5_feature_detection/examples/05_corner_detection.py`](./experiments/5_feature_detection/examples/05_corner_detection.py)

### 5.2. Contours
- **Key Idea:** Contours are the outlines of objects. Analyzing contours allows you to calculate properties like area, perimeter, center point (centroid), and geometric shape.
- **Relevant Scripts:**
  - [`./experiments/5_feature_detection/examples/06_find_and_draw_contours.py`](./experiments/5_feature_detection/examples/06_find_and_draw_contours.py)
  - [`./experiments/5_feature_detection/examples/07_contour_properties.py`](./experiments/5_feature_detection/examples/07_contour_properties.py)
  - [`./experiments/5_feature_detection/examples/08_convex_hull.py`](./experiments/5_feature_detection/examples/08_convex_hull.py)
  - [`./experiments/5_feature_detection/examples/09_convexity_defects.py`](./experiments/5_feature_detection/examples/09_convexity_defects.py)

### 5.3. Hough Transform
- **Key Idea:** A powerful mathematical technique for detecting parametric shapes like lines and circles, even if they are broken or partially obscured.
- **Relevant Scripts:**
  - [`./experiments/5_feature_detection/examples/10_hough_lines.py`](./experiments/5_feature_detection/examples/10_hough_lines.py)
  - [`./experiments/5_feature_detection/examples/11_hough_lines_video.py`](./experiments/5_feature_detection/examples/11_hough_lines_video.py)
  - [`./experiments/5_feature_detection/examples/12_hough_circles.py`](./experiments/5_feature_detection/examples/12_hough_circles.py)

---

## 6. Applications and Exercises

This is where all the concepts come together to build practical applications.

- **Object Isolation/Tracking by Color:**
  - [`./experiments/5_feature_detection/examples/08_object_isolation_by_color.py`](./experiments/5_feature_detection/examples/08_object_isolation_by_color.py)
  - [`./experiments/6_applications_and_exercises/examples/07_skin_color_object_detection.py`](./experiments/6_applications_and_exercises/examples/07_skin_color_object_detection.py)
- **Shape Detection (Static & Real-time):**
  - [`./experiments/6_applications_and_exercises/examples/03_static_shape_detection.py`](./experiments/6_applications_and_exercises/examples/03_static_shape_detection.py)
  - [`./experiments/6_applications_and_exercises/examples/04_real_time_shape_detection.py`](./experiments/6_applications_and_exercises/examples/04_real_time_shape_detection.py)
- **Background Subtraction:**
  - [`./experiments/6_applications_and_exercises/examples/05_manual_bg_subtraction.py`](./experiments/6_applications_and_exercises/examples/05_manual_bg_subtraction.py)
  - [`./experiments/6_applications_and_exercises/examples/06_mog2_bg_subtraction.py`](./experiments/6_applications_and_exercises/examples/06_mog2_bg_subtraction.py)
- **Advanced Applications:**
  - [`./experiments/6_applications_and_exercises/examples/08_hand_gesture_recognition.py`](./experiments/6_applications_and_exercises/examples/08_hand_gesture_recognition.py)
  - [`./experiments/6_applications_and_exercises/examples/09_pupil_tracking_simulation.py`](./experiments/6_applications_and_exercises/examples/09_pupil_tracking_simulation.py)
  - [`./experiments/6_applications_and_exercises/examples/10_image_comparison.py`](./experiments/6_applications_and_exercises/examples/10_image_comparison.py)