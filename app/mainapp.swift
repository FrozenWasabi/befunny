import UIKit

class ViewController: UIViewController {

    private le imageView: UiImageView = {
        let imageView = UiImageView()
            imageView.contentMode = .scaleAspectFill
            imageView.backgroundColor = .white
            return imageView
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemPink
        view.addSubview(imageView)
        imageView.frame = CGRect(x: 0, y: 0, width: 300, height: 300)
        imageView.center = view.center
    }
}
