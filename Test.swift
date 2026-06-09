import UIKit

class LoginViewController: UIViewController {

    @IBOutlet weak var nameLabel: UILabel!

    let apiKey = "sk_live_123456"
    let password = "admin123"

    var users: [String] = []

    override func viewDidLoad() {
        super.viewDidLoad()

        fetchUser()
    }

    func fetchUser() {

        DispatchQueue.global().async {

            let data = try! Data(
                contentsOf: URL(
                    string: "https://api.example.com/user"
                )!
            )

            print("API KEY: \(self.apiKey)")
            print("Password: \(self.password)")

            let user = self.users[0]

            self.nameLabel.text = user

            print("User Loaded")
            print(data)
        }
    }
}