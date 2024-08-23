# 🍕 ProfilePizza
### Video Demo: <url>

### Description:
A fun and creative tool for generating dynamic profiles on GitHub!
ProfilePizza helps you fill your GitHub profile with dynamic and engaging text. This program automatically generates a personalized and amusing text based on your recent commits and projects. Say goodbye to repetitive profile writing and easily showcase your skills and experiences!


### Why ProfilePizza?
Because every coder has their own story, and we want to serve it up in a deliciously engaging way!

---

## Usage

To generate an SVG image, make a GET request to the `svg_generator` view with the following parameters:

- `username`: Your GitHub username.
- `bgcolor`: Background color in hex format (default: `#f4f4f4`).
- `textcolor`: Text color in hex format (default: complementary color of `bgcolor`).
- `no_bg`: Boolean value to exclude background (default: `false`).
- `width`: Width of the SVG image (default: `600`).
- `height`: Height of the SVG image (default: `400`).
- `font_size`: Font size for the text (default: calculated based on width and height).

### Example Request


#### 1. Default Request

```http
GET https://profile-pizza.liara.run/generate/tahamusvi/
```
![Default Project Stats](https://profile-pizza.liara.run/generate/tahamusvi/)


#### 2. Background Color

```http
GET https://profile-pizza.liara.run/generate/tahamusvi/?bgcolor=000
```
![Black Background Project Stats](https://profile-pizza.liara.run/generate/tahamusvi/?bgcolor=000)

#### 3. Text Color

```http
GET https://profile-pizza.liara.run/generate/tahamusvi/?textcolor=646464
```
![Red Text Project Stats](https://profile-pizza.liara.run/generate/tahamusvi/?textcolor=646464)

#### 4. No Background

```http
GET https://profile-pizza.liara.run/generate/tahamusvi/?no_bg=true
```
![No Background Project Stats](https://profile-pizza.liara.run/generate/tahamusvi/?no_bg=true)

#### 5. Custom Width and Height

```http
GET https://profile-pizza.liara.run/generate/tahamusvi/?width=800&height=600
```
![Custom Size Project Stats](https://profile-pizza.liara.run/generate/tahamusvi/?width=800&height=600)

#### 6. Custom Font Size

```http
GET https://profile-pizza.liara.run/generate/tahamusvi/?font_size=30
```
![Larger Font Size Project Stats](https://profile-pizza.liara.run/generate/tahamusvi/?font_size=30)


## Support

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/yourusername/yourrepository).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Special thanks to the GitHub API for providing user data and to the open-source community for their contributions.
