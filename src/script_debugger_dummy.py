class WildfirePredictor(nn.Module):
    def __init__(
        self,
        input_channels=4,
        conv1_channels=6,
        conv2_channels=12,
        lstm_hidden_size=64,
        output_size=(300, 300),
    ):
        super(WildfirePredictor, self).__init__()
        self.input_channels = input_channels
        self.conv1_channels = conv1_channels
        self.conv2_channels = conv2_channels
        self.lstm_hidden_size = lstm_hidden_size
        self.output_size = output_size
        conv_output_dim = (output_size[0] // 4, output_size[1] // 4)

        self.conv1 = nn.Conv2d(
            input_channels, conv1_channels, kernel_size=3, stride=2, padding=1
        )
        self.conv2 = nn.Conv2d(
            conv1_channels, conv2_channels, kernel_size=3, stride=2, padding=1
        )
        self.lstm = nn.LSTM(
            input_size=conv2_channels * conv_output_dim[0] * conv_output_dim[1],
            hidden_size=lstm_hidden_size,
            batch_first=True,
        )
        self.fc = nn.Linear(lstm_hidden_size, output_size[0] * output_size[1])

    def forward(self, x):
        batch_size, timesteps, C, H, W = x.size()

        processed_steps = []
        for i in range(timesteps):
            step = F.relu(self.conv1(x[:, i]))
            step = F.relu(self.conv2(step))
            step = step.view(batch_size, -1)
            processed_steps.append(step)

        lstm_input = torch.stack(processed_steps, dim=1)
        lstm_out, (h_n, c_n) = self.lstm(lstm_input)

        out = self.fc(lstm_out[:, -1])
        out = out.view(batch_size, 300, 300)
        out = torch.sigmoid(out)
        return out
