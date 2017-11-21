# Kaggle Project for Applied Machine Learning

Deadline for the project is December 11<sup>th</sup> 2017. 

## The project

### Predicting Ocean Health [(link)](https://www.kaggle.com/c/1stdsbowl-in-class)

Plankton are critically important to our ecosystem, accounting for more than half the primary productivity on earth and nearly half the total carbon fixed in the global carbon cycle. They form the foundation of aquatic food webs including those of large, important fisheries. Loss of plankton populations could result in ecological upheaval as well as negative societal impacts, particularly in indigenous cultures and the developing world. Plankton’s global significance makes their population levels an ideal measure of the health of the world’s oceans and ecosystems.

Traditional methods for measuring and monitoring plankton populations are time consuming and cannot scale to the granularity or scope necessary for large-scale studies. Improved approaches are needed. One such approach is through the use of an underwater imagery sensor. This towed, underwater camera system captures microscopic, high-resolution images over large study areas. The images can then be analyzed to assess species populations and distributions.

Manual analysis of the imagery is infeasible – it would take a year or more to manually analyze the imagery volume captured in a single day. Automated image classification using machine learning tools is an alternative to the manual approach. Analytics will allow analysis at speeds and scales previously thought impossible. The automated system will have broad applications for assessment of ocean and ecosystem health.

The National Data Science Bowl challenges you to build an algorithm to automate the image identification process. Scientists at the Hatfield Marine Science Center and beyond will use the algorithms you create to study marine food webs, fisheries, ocean conservation, and more. This is your chance to contribute to the health of the world’s oceans, one plankton at a time.

### Evaluation

Submissions are evaluated using the category accuracy. Each image has been labeled with one true class. For each image, you must submit your predicted class. The formula is then:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mi>C</mi>
  <mi>a</mi>
  <mi>t</mi>
  <mi>e</mi>
  <mi>g</mi>
  <mi>o</mi>
  <mi>r</mi>
  <mi>y</mi>
  <mi>A</mi>
  <mi>c</mi>
  <mi>c</mi>
  <mi>u</mi>
  <mi>r</mi>
  <mi>a</mi>
  <mi>c</mi>
  <mi>y</mi>
  <mo>=</mo>
  <mfrac>
    <mn>1</mn>
    <mi>N</mi>
  </mfrac>
  <munder>
    <mo>&#x2211;<!-- ∑ --></mo>
    <mrow class="MJX-TeXAtom-ORD">
      <msub>
        <mi>y</mi>
        <mi>i</mi>
      </msub>
      <mo>=</mo>
      <msub>
        <mrow class="MJX-TeXAtom-ORD">
          <mover>
            <mi>y</mi>
            <mo stretchy="false">&#x005E;<!-- ^ --></mo>
          </mover>
        </mrow>
        <mi>i</mi>
      </msub>
    </mrow>
  </munder>
  <mn>1</mn>
  <mo>,</mo>
</math>

where N is the number of images in the test set, yiyi is the true label for the i-th image, and ŷ iy^i is the predicted label.

### Submission Format

You must submit a csv file with the image name and the predicted class label. The order of the rows does not matter. The file must have a header and should look like the following:

```
image,class
1.jpg,0
10.jpg,99
...
etc
```

## Goal

What we need to do:

* Choose one of the projects
* Load and preprocess data
* Extract features
* Train models
* Evaluate models
* Find and implement improvements

## Required packages

All the required packages can be installed with the following command:

```pip install -r requirements.txt```